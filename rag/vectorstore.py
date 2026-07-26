import os

from langchain_community.vectorstores import FAISS

from rag.embeddings import get_embedding_model


embedding = get_embedding_model()


def create_or_update_vectorstore(chunks, user_id):

    folder = f"vectorstore/user_{user_id}"

    os.makedirs(folder, exist_ok=True)

    index_file = os.path.join(folder, "index.faiss")

    if os.path.exists(index_file):

        db = FAISS.load_local(

            folder,

            embedding,

            allow_dangerous_deserialization=True

        )

        db.add_documents(chunks)

    else:

        db = FAISS.from_documents(

            chunks,

            embedding

        )

    db.save_local(folder)


def load_vectorstore(user_id):

    folder = f"vectorstore/user_{user_id}"

    if not os.path.exists(folder):

        return None

    return FAISS.load_local(

        folder,

        embedding,

        allow_dangerous_deserialization=True

    )