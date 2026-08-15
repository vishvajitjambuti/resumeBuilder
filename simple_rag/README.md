# Simple RAG (Retrieval-Augmented Generation)

A minimal, dependency-light RAG system in Python. No API keys or internet
access required to run it — retrieval uses TF-IDF (scikit-learn) instead of
a neural embedding model, so the whole pipeline runs offline.

## What RAG means here

1. **Chunk & Store** — text (from files or raw strings) is split into
   overlapping chunks and saved to disk as JSON.
2. **Retrieve** — a question is compared against every stored chunk using
   TF-IDF + cosine similarity; the most relevant chunks are pulled out.
3. **Augment** — those chunks are assembled into a "context" block.
4. **Generate** — an answer is produced from that context. By default this
   is *extractive* (it returns the best-matching chunk verbatim) so the
   project needs zero API keys. If you set `ANTHROPIC_API_KEY` in your
   environment, it will automatically use Claude to write a proper
   synthesized answer instead.

## File structure

```
simple_rag/
├── main.py                    # end-to-end demo: add files + text, then ask questions
├── add_document.py            # CLI: add a .txt file (or folder) to the RAG
├── query.py                   # CLI: ask a question to the RAG
├── data/                      # sample source documents
│   ├── company_policy.txt
│   └── product_faq.txt
├── storage/
│   └── documents.json         # persisted chunk store (created on first run)
└── rag/                       # the actual library code
    ├── __init__.py            # exposes RAGEngine
    ├── document_store.py      # chunking + JSON persistence
    ├── embedder.py            # TF-IDF vectorization + cosine similarity search
    └── rag_engine.py          # orchestrates store + embedder, add/query API
```

### How the pieces fit together

- **`document_store.py`** only knows about text and disk. It splits text
  into ~500-character chunks (with 100-char overlap so sentences on chunk
  boundaries aren't lost), assigns each an id, and saves/loads them as JSON.
- **`embedder.py`** only knows about vectors. It fits a TF-IDF matrix over
  every chunk currently in the store, and can score a new query against
  that matrix to return the top-k most similar chunk indices.
- **`rag_engine.py`** is the glue: it re-fits the embedder any time new
  data is added, and implements `query()` = retrieve → augment → generate.
- **`add_document.py`** / **`query.py`** are thin CLIs on top of `RAGEngine`.

## Usage

```bash
cd simple_rag

# 1. Add a text file to the RAG
python add_document.py data/company_policy.txt
python add_document.py data/product_faq.txt

# (You can also add every .txt in a folder at once)
python add_document.py data/

# 2. Ask a question
python query.py "What is the refund policy?"

# Or run the full demo (adds files + raw text, then asks 4 questions)
python main.py
```

## Adding data programmatically

```python
from rag import RAGEngine

engine = RAGEngine()
engine.add_file("data/company_policy.txt")     # from a file
engine.add_text("Some raw string of data...")   # from a plain string
result = engine.query("your question")
print(result["answer"])
print(result["sources"])
```

## Notes / how to extend this

- **Swap in real embeddings:** replace the internals of `embedder.py`
  (e.g. use `sentence-transformers` or an embeddings API) and store vectors
  in a proper vector index (FAISS, Chroma, pgvector). `document_store.py`
  and `rag_engine.py` don't need to change since they only depend on
  `fit()` / `top_k()` existing.
- **Swap in real generation:** `rag_engine.py` already has an
  `_generate_with_llm()` method wired up for the Anthropic API — it's used
  automatically if `ANTHROPIC_API_KEY` is set in your environment.
- **Chunk size/overlap** are configurable via
  `DocumentStore.chunk_text(text, chunk_size=500, overlap=100)`.
- **Scale:** TF-IDF refits on the *entire* corpus every time you add data,
  which is fine for demos/small corpora but not for large-scale use —
  at that point move to a real vector database with incremental indexing.
