# backend/server/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .logic import analyse_text as compute_score

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextRequest(BaseModel):
    text: str


@app.post("/analyse")
def analyse_text(request: TextRequest):
    score, explanation = compute_score(request.text)

    return {
        "ai_score": score,
        "explanation": explanation,
    }
