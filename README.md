# ai-qa-api
# AI Q&A API

An AI-powered question-answering REST API built with FastAPI, Groq LLM, and PostgreSQL.

## Live Demo
https://ai-qa-api-2c9n.onrender.com

## API Documentation
https://ai-qa-api-2c9n.onrender.com/docs

## Features
- REST API built with FastAPI
- LLM integration using Groq (Llama 3.1)
- PostgreSQL database for document storage
- Cloud deployed on Render

## API Endpoints

### GET /
Returns API status.

### POST /ask
Ask a question and get an AI-powered answer.

**Request:**
```json
{"question": "Who is Namitha?"}
{"answer": "Namitha K is a Data Analyst..."}
