# backend/server/main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel


app = FastAPI()

class TextRequest(BaseModel):
    text: str



@app.post("/analyse")
def analyse_text(request: TextRequest):
    score = 78

    return {
        "ai_score": score,
        "explanation": "This text is AI written due to..."
    }


