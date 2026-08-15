"""
rag_engine.py
-------------
The orchestrator. This is the file the rest of the world (CLI scripts,
your own app) talks to. It hides the fact that there are two moving
parts underneath (DocumentStore + Embedder) behind one simple API:

    engine = RAGEngine()
    engine.add_file("notes.txt")
    engine.add_text("some raw text")
    result = engine.query("What is X?")

Pipeline for `query()` (this IS what "RAG" means):
    1. RETRIEVE : embed the question, find the most similar stored chunks
    2. AUGMENT  : stuff those chunks into a prompt as "context"
    3. GENERATE : produce an answer using that context
                  (extractive by default; pluggable LLM if you want one)
"""

from __future__ import annotations
import os
from typing import Dict, List, Optional

from .document_store import DocumentStore
from .embedder import Embedder


class RAGEngine:
    def __init__(self, storage_path: str = "storage/documents.json"):
        self.store = DocumentStore(storage_path=storage_path)
        self.embedder = Embedder()
        self._reindex()  # build TF-IDF index from whatever was already on disk

    # ------------------------------------------------------------------ #
    # Indexing helpers
    # ------------------------------------------------------------------ #
    def _reindex(self) -> None:
        """Rebuild the TF-IDF index from every chunk currently in the store."""
        texts = [c["text"] for c in self.store.all_chunks()]
        self.embedder.fit(texts)

    # ------------------------------------------------------------------ #
    # Ingestion ("add data to the RAG")
    # ------------------------------------------------------------------ #
    def add_text(self, text: str, source: str = "manual_input") -> int:
        """Add raw text (e.g. pasted string, scraped content) to the RAG."""
        n = self.store.add_text(text, source=source)
        self._reindex()
        return n

    def add_file(self, filepath: str) -> int:
        """Add a .txt file's contents to the RAG."""
        n = self.store.add_file(filepath)
        self._reindex()
        return n

    def add_folder(self, folder_path: str) -> int:
        """Add every .txt file found in a folder."""
        total = 0
        for fname in os.listdir(folder_path):
            if fname.lower().endswith(".txt"):
                total += self.add_file(os.path.join(folder_path, fname))
        return total

    # ------------------------------------------------------------------ #
    # Querying ("ask a question to the RAG")
    # ------------------------------------------------------------------ #
    def retrieve(self, question: str, k: int = 3) -> List[Dict]:
        """Return the top-k most relevant chunks for `question`."""
        chunks = self.store.all_chunks()
        hits = self.embedder.top_k(question, k=k)
        results = []
        for idx, score in hits:
            chunk = dict(chunks[idx])
            chunk["score"] = round(score, 4)
            results.append(chunk)
        return results

    def query(self, question: str, k: int = 3, use_llm: Optional[bool] = None) -> Dict:
        """
        Full RAG pipeline: retrieve relevant chunks, then generate an answer.

        use_llm:
            None  -> auto: use Claude if ANTHROPIC_API_KEY env var is set,
                     otherwise fall back to a simple extractive answer.
            True  -> force LLM (raises if no API key available)
            False -> force the extractive fallback (no API calls at all)
        """
        retrieved = self.retrieve(question, k=k)

        if not retrieved:
            return {
                "question": question,
                "answer": "I don't have any relevant information for that yet. "
                          "Add some documents first.",
                "sources": [],
            }

        context = "\n\n".join(
            f"[{c['source']} #{c['chunk_index']}] {c['text']}" for c in retrieved
        )

        should_use_llm = use_llm if use_llm is not None else bool(os.environ.get("ANTHROPIC_API_KEY"))

        if should_use_llm:
            answer = self._generate_with_llm(question, context)
        else:
            answer = self._generate_extractive(question, retrieved)

        return {
            "question": question,
            "answer": answer,
            "sources": [
                {"source": c["source"], "chunk_index": c["chunk_index"], "score": c["score"]}
                for c in retrieved
            ],
        }

    # ------------------------------------------------------------------ #
    # Generation strategies
    # ------------------------------------------------------------------ #
    @staticmethod
    def _generate_extractive(question: str, retrieved: List[Dict]) -> str:
        """
        No-LLM fallback: just surface the best-matching chunk(s) as the
        "answer". This keeps the whole project runnable with zero API keys
        and zero internet access, so the RETRIEVAL half of RAG can be
        demonstrated/tested in isolation from generation.
        """
        best = retrieved[0]
        return (
            f"(extractive answer, top match from '{best['source']}', "
            f"similarity={best['score']}):\n\"{best['text']}\""
        )

    @staticmethod
    def _generate_with_llm(question: str, context: str) -> str:
        """
        Real generation step using the Anthropic API. Only called if
        ANTHROPIC_API_KEY is set (or use_llm=True is passed explicitly).
        """
        import anthropic  # imported lazily so the package isn't a hard dependency

        client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env
        prompt = (
            "Answer the question using ONLY the context below. "
            "If the context doesn't contain the answer, say so.\n\n"
            f"Context:\n{context}\n\nQuestion: {question}"
        )
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text
