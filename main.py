from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os

app = FastAPI()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

documents = [
    "Namitha K is a Data Analyst with expertise in Python, Power BI, and Machine Learning.",
    "She completed her B.Tech in Electrical and Electronics Engineering.",
    "She has a Google Cloud Data Analytics Certificate.",
    "She did an internship at Techolas Technology as a Data Analyst.",
    "Her projects include Google Play Store Analysis, Adidas Sales Performance, and EV Charging Demand Prediction."
]

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "AI Q&A API is running!"}

@app.post("/ask")
def ask(q: Question):
    context = "\n".join(documents)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": f"Answer based on this info:\n{context}"},
            {"role": "user", "content": q.question}
        ]
    )
    return {"answer": response.choices[0].message.content}