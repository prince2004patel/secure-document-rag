# 🔒 Secure Document Query System using RAG

## Overview

The Secure Document Query System is a Retrieval-Augmented Generation (RAG) application that enables users to upload documents and ask questions in natural language. Instead of relying on the LLM's general knowledge, the system retrieves relevant information from the uploaded documents and generates accurate, context-aware answers.

The application is designed with security as a priority by ensuring that each user's documents remain completely isolated and that sensitive information is protected before being indexed.

## Problem Statement

Organizations manage large volumes of documents such as contracts, employee records, financial reports, and customer documents. Searching through these files manually is time-consuming and inefficient.

Traditional AI chatbots may also expose confidential information or mix data between different users if proper security measures are not implemented.

This project addresses these challenges by providing a secure document querying system built on a Retrieval-Augmented Generation (RAG) pipeline.

## Objectives

- Build a secure document question-answering system.
- Allow users to upload PDF and DOCX documents.
- Generate answers using only the uploaded documents.
- Prevent data leakage between different users.
- Protect confidential information before indexing documents.
- Demonstrate a scalable and modular RAG architecture.

## Key Features

- User Registration and Login
- Upload PDF and DOCX documents
- Retrieval-Augmented Generation (RAG)
- Semantic search using FAISS Vector Database
- Hugging Face Embeddings for document representation
- Groq LLM for answer generation
- User-specific document isolation
- Sensitive information masking
- Source-aware responses
- Interactive Streamlit interface
- Flask REST API backend

## How the System Works

1. A user registers and logs into the application.
2. The user uploads one or more documents.
3. The system extracts text from the uploaded documents.
4. Sensitive information such as passwords and client IDs is masked.
5. The text is split into smaller chunks.
6. Embeddings are generated for each chunk.
7. The embeddings are stored in a user-specific FAISS vector database.
8. When a question is asked, the system retrieves the most relevant document chunks.
9. The retrieved context is sent to the Groq Large Language Model.
10. The generated answer is returned along with the source document.

## Security Features

- Passwords are stored securely using Bcrypt hashing.
- Sensitive information is masked before vector indexing.
- Each user has an independent vector database.
- Documents from one user cannot be accessed by another user.
- Protected information is never disclosed through the chatbot.

## Technologies Used

### Frontend

- Streamlit

### Backend

- Flask
- Flask-CORS

### Database

- SQLite
- SQLAlchemy

### RAG Pipeline

- LangChain
- FAISS
- Hugging Face Embeddings
- Groq LLM

### Security

- Bcrypt
- Regular Expressions (Regex)
- User-specific document isolation

## Example Questions

- What is the employee's name?
- Who is the manager?
- What are the employee's responsibilities?
- What services are included in the contract?
- When does the contract expire?

Sensitive questions such as passwords or client IDs are automatically blocked to ensure data privacy.

## Future Enhancements

- JWT Authentication
- OCR support for scanned documents
- PostgreSQL or MySQL integration
- Cloud storage support
- Docker deployment
- Multi-document filtering
- Chat history
- Role-based access control
- Production deployment on Render or AWS

## Project Files

| File / Folder                  | Description                                                                         |
| ------------------------------ | ----------------------------------------------------------------------------------- |
| **app.py**                     | Main Flask application that initializes the backend, database, and API routes.      |
| **frontend/streamlit_app.py**  | Streamlit user interface for login, document upload, and document querying.         |
| **routes/auth.py**             | Handles user registration and login APIs.                                           |
| **routes/upload.py**           | Handles document upload and stores document information.                            |
| **routes/query.py**            | Processes user questions and returns answers from the RAG pipeline.                 |
| **database/db.py**             | Configures the SQLite database connection.                                          |
| **database/models.py**         | Defines database models for users and uploaded documents.                           |
| **rag/loader.py**              | Loads PDF and DOCX documents into the application.                                  |
| **rag/splitter.py**            | Splits documents into smaller text chunks for retrieval.                            |
| **rag/embeddings.py**          | Generates vector embeddings using Hugging Face models.                              |
| **rag/vectorstore.py**         | Creates and manages the FAISS vector database.                                      |
| **rag/retriever.py**           | Retrieves the most relevant document chunks based on the user's question.           |
| **rag/llm.py**                 | Configures and initializes the Groq Large Language Model.                           |
| **rag/pipeline.py**            | Implements the complete RAG workflow from document processing to answer generation. |
| **security/auth_utils.py**     | Provides password hashing and verification using Bcrypt.                            |
| **security/masking.py**        | Masks sensitive information before document indexing.                               |
| **security/regex_patterns.py** | Contains regex patterns used to detect confidential information.                    |
| **uploads/**                   | Stores uploaded documents for each user.                                            |
| **vectorstore/**               | Stores user-specific FAISS vector databases.                                        |
| **instance/users.db**          | SQLite database containing user accounts and document metadata.                     |
| **requirements.txt**           | Lists all Python dependencies required to run the project.                          |
| **.env**                       | Stores environment variables such as API keys and secret keys.                      |
| **README.md**                  | Project documentation and usage instructions.                                       |
