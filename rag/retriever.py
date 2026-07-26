from rag.vectorstore import load_vectorstore


def retrieve(user_id, question):

    db = load_vectorstore(user_id)

    if db is None:

        return []

    retriever = db.as_retriever(

        search_kwargs={

            "k":4

        }

    )

    return retriever.invoke(question)