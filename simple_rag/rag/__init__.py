"""
Simple RAG (Retrieval-Augmented Generation) package.

Modules:
    document_store  -> stores/chunks/persists documents
    embedder         -> turns text into vectors (TF-IDF) + similarity search
    rag_engine       -> ties store + embedder together, exposes add/query API
"""

from .rag_engine import RAGEngine

__all__ = ["RAGEngine"]
