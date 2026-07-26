import os

from rag.loader import load_document
from rag.splitter import split_documents
from rag.vectorstore import create_or_update_vectorstore
from rag.retriever import retrieve
from rag.llm import get_llm

from security.masking import mask_sensitive_data


def process_document(file_path, user_id):

    documents = load_document(file_path)

    for doc in documents:
        doc.page_content = mask_sensitive_data(
            doc.page_content
        )

    chunks = split_documents(documents)

    create_or_update_vectorstore(
        chunks,
        user_id
    )


def answer_question(user_id, question):

    # -----------------------------
    # Security Check
    # -----------------------------
    question_lower = question.lower()

    sensitive_keywords = [
        "password",
        "client id",
        "clientid",
        "email",
        "phone",
        "mobile",
        "aadhaar",
        "pan",
        "employee id",
        "emp id",
        "personal information"
    ]

    for keyword in sensitive_keywords:
        if keyword in question_lower:
            return {
                "answer": "This information is protected and cannot be disclosed for security reasons.",
                "sources": []
            }

    # -----------------------------
    # Retrieve Documents
    # -----------------------------
    docs = retrieve(
        user_id,
        question
    )

    if len(docs) == 0:
        return {
            "answer": "No document found for this user.",
            "sources": []
        }

    # -----------------------------
    # Build Context
    # -----------------------------
    context = ""

    sources = set()

    for doc in docs:

        context += doc.page_content + "\n\n"

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        sources.add(
            os.path.basename(source)
        )

    # -----------------------------
    # Prompt
    # -----------------------------
    prompt = f"""
You are a secure document assistant.

Rules:

1. Answer ONLY using the provided context.

2. If the answer is not available in the context, reply exactly:
"I could not find that information."

3. Never guess or make up information.

4. Never reveal sensitive information such as:
- Passwords
- Client IDs
- Email addresses
- Phone numbers
- Aadhaar Numbers
- PAN Numbers
- Employee IDs

5. Give concise and professional answers.

Context:
{context}

Question:
{question}

Answer:
"""

    # -----------------------------
    # Generate Answer
    # -----------------------------
    response = get_llm().invoke(prompt)

    return {
        "answer": response.content,
        "sources": list(sources)
    }