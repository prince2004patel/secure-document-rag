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

    docs = retrieve(

        user_id,

        question

    )

    if len(docs) == 0:

        return {

            "answer":"No document found for this user.",

            "sources":[]

        }

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

    prompt = f"""

You are a secure document assistant.

Rules:

1. Only answer using the provided context.

2. Never guess.

3. If the answer is unavailable reply:

'I could not find that information.'

4. Never reveal masked information.

Context:

{context}

Question:

{question}

"""

    response = get_llm().invoke(prompt)

    return {

        "answer":response.content,

        "sources":list(sources)

    }