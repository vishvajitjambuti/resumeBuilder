"""
add_document.py
----------------
CLI: add a .txt file (or a folder of .txt files) to the RAG's storage.

Usage:
    python add_document.py data/sample1.txt
    python add_document.py data/                 # adds every .txt in the folder
"""

import sys
import os
from rag import RAGEngine


def main():
    if len(sys.argv) != 2:
        print("Usage: python add_document.py <path-to-txt-file-or-folder>")
        sys.exit(1)

    path = sys.argv[1]
    engine = RAGEngine()

    if os.path.isdir(path):
        n = engine.add_folder(path)
        print(f"Added {n} chunks from all .txt files in '{path}'")
    elif os.path.isfile(path):
        n = engine.add_file(path)
        print(f"Added {n} chunks from '{path}'")
    else:
        print(f"Path not found: {path}")
        sys.exit(1)

    print(f"Total chunks now in store: {len(engine.store)}")


if __name__ == "__main__":
    main()
