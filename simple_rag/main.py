"""
main.py
-------
End-to-end demo of the whole pipeline in one script:

    1. Create the RAG engine
    2. Add text FILES to it        (data/company_policy.txt, data/product_faq.txt)
    3. Add raw TEXT DATA to it     (a string, not from a file)
    4. Ask it several QUESTIONS and print the retrieved answers + sources

Run with:  python main.py
"""

from rag import RAGEngine


def main():
    print("=" * 70)
    print("STEP 1: Initialize the RAG engine")
    print("=" * 70)
    engine = RAGEngine(storage_path="storage/documents.json")
    print(f"Engine ready. Chunks currently stored: {len(engine.store)}\n")

    print("=" * 70)
    print("STEP 2: Add text FILES to the RAG")
    print("=" * 70)
    for filepath in ["data/company_policy.txt", "data/product_faq.txt"]:
        n = engine.add_file(filepath)
        print(f"  + {filepath} -> {n} chunks added")

    print("\n" + "=" * 70)
    print("STEP 3: Add raw TEXT DATA to the RAG (no file needed)")
    print("=" * 70)
    raw_text = (
        "Business Hours: Our office is open Monday through Friday, "
        "9 AM to 6 PM Eastern Time. We are closed on major US holidays. "
        "Live chat support remains available 24/7 regardless of office hours."
    )
    n = engine.add_text(raw_text, source="business_hours_note")
    print(f"  + raw text -> {n} chunks added")

    print(f"\nTotal chunks now indexed: {len(engine.store)}\n")

    print("=" * 70)
    print("STEP 4: Ask questions to the RAG")
    print("=" * 70)
    questions = [
        "What is the refund policy?",
        "How do I reset my password?",
        "What are your business hours?",
        "Does the warranty cover water damage?",
    ]

    for q in questions:
        result = engine.query(q, k=2)
        print(f"\nQ: {result['question']}")
        print(f"A: {result['answer']}")
        print("Sources:")
        for s in result["sources"]:
            print(f"   - {s['source']} (chunk #{s['chunk_index']}, score={s['score']})")

    print("\n" + "=" * 70)
    print("Done. Storage persisted at storage/documents.json")
    print("=" * 70)


if __name__ == "__main__":
    main()
