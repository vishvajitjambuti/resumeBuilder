"""
embedder.py
-----------
Responsible for turning text into vectors, and finding the most similar
vectors to a query. This is the "R" (Retrieval) in RAG.

We use TF-IDF (Term Frequency - Inverse Document Frequency) instead of a
neural embedding model on purpose:
    - No model download / API key / GPU required -- runs fully offline.
    - Good enough to demonstrate the RAG *pattern* clearly.
    - Swappable: see the note at the bottom of this file for how you'd
      plug in a real embedding model (OpenAI, sentence-transformers, etc.)
      later without touching any other file.
"""

from __future__ import annotations
from typing import List, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Embedder:
    def __init__(self):
        # min_df=1 so it works even with very few chunks (e.g. in demos/tests)
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = None          # TF-IDF matrix of all indexed chunks
        self.is_fitted = False

    def fit(self, texts: List[str]) -> None:
        """(Re)build the TF-IDF matrix from the full current set of chunks.

        TF-IDF needs to see the whole corpus at once to compute document
        frequencies, so every time new text is added we simply refit on
        everything. Fine for small/medium corpora; a production system
        would use an incremental vector index (e.g. FAISS) instead.
        """
        if not texts:
            self.matrix = None
            self.is_fitted = False
            return
        self.matrix = self.vectorizer.fit_transform(texts)
        self.is_fitted = True

    def top_k(self, query: str, k: int = 3) -> List[Tuple[int, float]]:
        """
        Return the indices (into the `texts` list passed to `fit`) of the
        `k` most similar chunks to `query`, along with their similarity
        scores (0..1), sorted highest similarity first.
        """
        if not self.is_fitted:
            return []

        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.matrix)[0]

        # argsort ascending -> reverse for descending -> take top k
        ranked = scores.argsort()[::-1][:k]
        return [(int(i), float(scores[i])) for i in ranked if scores[i] > 0]


# ---------------------------------------------------------------------- #
# Swapping in a real embedding model later:
#
#   Replace `fit`/`top_k` internals with calls to e.g. sentence-transformers
#   (`model.encode(texts)`) or an embeddings API, store vectors in a proper
#   vector index (FAISS/Chroma/pgvector), and do cosine/dot-product search
#   there. The rest of this project (document_store.py, rag_engine.py)
#   would not need to change, since they only depend on `fit()` and
#   `top_k()` existing with this signature.
# ---------------------------------------------------------------------- #
