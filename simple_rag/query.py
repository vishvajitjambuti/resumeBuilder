"""
query.py
--------
CLI: ask a question to the RAG.

Usage:
    python query.py "What is the refund policy?"
"""

import sys
import json
from rag import RAGEngine


def main():
    if len(sys.argv) < 2:
        print('Usage: python query.py "your question here"')
        sys.exit(1)

    question = " ".join(sys.argv[1:])
    engine = RAGEngine()
    result = engine.query(question, k=3)

    print("\nQ:", result["question"])
    print("\nA:", result["answer"])
    print("\nSources used:")
    print(json.dumps(result["sources"], indent=2))


if __name__ == "__main__":
    main()
