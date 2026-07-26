from flask import Blueprint
from flask import request
from flask import jsonify

from rag.pipeline import answer_question

query_bp = Blueprint(
    "query",
    __name__
)


@query_bp.route(
    "/query",
    methods=["POST"]
)
def query():

    data = request.get_json()

    user_id = data.get(
        "user_id"
    )

    question = data.get(
        "question"
    )

    if not question:

        return jsonify({
            "error":"Question required."
        }),400

    result = answer_question(
        user_id,
        question
    )

    return jsonify(result)