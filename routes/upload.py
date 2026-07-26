import os
import uuid

from flask import Blueprint
from flask import request
from flask import jsonify

from database.db import db
from database.models import Document

from rag.pipeline import process_document

upload_bp = Blueprint(
    "upload",
    __name__
)

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@upload_bp.route(
    "/upload",
    methods=["POST"]
)
def upload():

    if "file" not in request.files:

        return jsonify({
            "error": "No file uploaded."
        }),400

    uploaded_file = request.files["file"]

    user_id = request.form.get("user_id")

    if uploaded_file.filename == "":

        return jsonify({
            "error":"No selected file."
        }),400

    user_folder = os.path.join(
        UPLOAD_FOLDER,
        f"user_{user_id}"
    )

    os.makedirs(
        user_folder,
        exist_ok=True
    )

    unique_filename = (
        str(uuid.uuid4())
        + "_"
        + uploaded_file.filename
    )

    filepath = os.path.join(
        user_folder,
        unique_filename
    )

    uploaded_file.save(filepath)

    process_document(
        filepath,
        user_id
    )

    document = Document(

        user_id=user_id,

        filename=uploaded_file.filename,

        filepath=filepath
    )

    db.session.add(document)

    db.session.commit()

    return jsonify({

        "message":"Document uploaded successfully.",

        "filename":uploaded_file.filename

    })