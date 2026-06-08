from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os
import psycopg2

app = FastAPI()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db():
    return psycopg2.connect(DATABASE_URL)

def setup_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL
        )
    """)
    cur.execute("SELECT COUNT(*) FROM documents")
    count = cur.fetchone()[0]
    if count == 0:
        docs = [
            "Namitha K is a Data Analyst with expertise in Python, Power BI, and Machine Learning.",
            "She completed her B.Tech in Electrical and Electronics Engineering.",
            "She has a Google Cloud Data Analytics Certificate.",
            "She did an internship at Techolas Technology as a Data Analyst.",
            "Her projects include Google Play Store Analysis, Adidas Sales Performance, and EV Charging Demand Prediction."
        ]
        for doc in docs:
            cur.execute("INSERT INTO documents (content) VALUES (%s)", (doc,))
    conn.commit()
    cur.close()
    conn.close()

setup_db()

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "AI Q&A API is running with PostgreSQL!"}

@app.post("/ask")
def ask(q: Question):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT content FROM documents")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    context = "\n".join([row[0] for row in rows])
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": f"Answer based on this info:\n{context}"},
            {"role": "user", "content": q.question}
        ]
    )
    return {"answer": response.choices[0].message.content}
