# ai-qa-api
# AI Q&A API

An AI-powered question-answering REST API built with FastAPI and Groq LLM.

## Live Demo
https://ai-qa-api-2c9n.onrender.com

## Features
- REST API built with FastAPI
- LLM integration using Groq (Llama 3.1)
- Embeddings-based document retrieval
- Deployed on Render

## API Endpoints

### GET /
Returns API status.

### POST /ask
Ask a question and get an AI answer.

**Request:**
```json
{"question": "Who is Namitha?"}

{"answer": "Namitha K is a Data Analyst..."}
