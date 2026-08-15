"""
document_store.py
------------------
Responsible for ONE thing: holding chunks of text on disk (as JSON) and
in memory, so the rest of the system doesn't need to know about files.

A "chunk" is a small dict:
    {
        "id": 3,                 # unique integer id
        "text": "...",           # the actual chunk text
        "source": "notes.txt",   # which file it came from
        "chunk_index": 0         # position of this chunk within that file
    }

Why chunk at all?
    Embedding (vectorizing) a whole 10-page file as ONE unit is useless for
    retrieval -- the vector becomes an average of everything in the file
    and loses the specific detail you're searching for. So every file is
    split into small overlapping windows of text ("chunks") and each chunk
    is embedded/stored/searched independently.
"""

from __future__ import annotations
import json
import os
from typing import List, Dict


class DocumentStore:
    def __init__(self, storage_path: str = "storage/documents.json"):
        self.storage_path = storage_path
        self.chunks: List[Dict] = []
        self._next_id = 0
        self._load()

    # ------------------------------------------------------------------ #
    # Persistence
    # ------------------------------------------------------------------ #
    def _load(self) -> None:
        """Load previously saved chunks from disk, if any exist."""
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.chunks = data.get("chunks", [])
                self._next_id = data.get("next_id", len(self.chunks))

    def _save(self) -> None:
        """Persist current chunks to disk as JSON."""
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(
                {"chunks": self.chunks, "next_id": self._next_id},
                f,
                ensure_ascii=False,
                indent=2,
            )

    # ------------------------------------------------------------------ #
    # Chunking
    # ------------------------------------------------------------------ #
    @staticmethod
    def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> List[str]:
        """
        Split text into overlapping windows of `chunk_size` characters.

        `overlap` characters are repeated between consecutive chunks so that
        a sentence sitting right on a chunk boundary isn't lost entirely
        from either chunk.
        """
        text = text.strip()
        if not text:
            return []

        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end].strip())
            if end >= len(text):
                break
            start = end - overlap  # step forward, but re-include the overlap
        return [c for c in chunks if c]

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #
    def add_text(self, text: str, source: str = "manual_input") -> int:
        """Chunk `text`, store each chunk, persist to disk. Returns #chunks added."""
        new_chunks = self.chunk_text(text)
        for i, chunk in enumerate(new_chunks):
            self.chunks.append(
                {
                    "id": self._next_id,
                    "text": chunk,
                    "source": source,
                    "chunk_index": i,
                }
            )
            self._next_id += 1
        self._save()
        return len(new_chunks)

    def add_file(self, filepath: str) -> int:
        """Read a .txt file and add its contents as chunks."""
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        source_name = os.path.basename(filepath)
        return self.add_text(text, source=source_name)

    def all_chunks(self) -> List[Dict]:
        return self.chunks

    def __len__(self) -> int:
        return len(self.chunks)
