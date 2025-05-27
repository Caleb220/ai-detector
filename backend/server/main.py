# backend/server/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


from .logic.ai_detection import score_ai_detection

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# BaseModel class for storing text content from user
class TextRequest(BaseModel):
    text: str



@app.post("/analyse")
def analyse_text(request: TextRequest):
    user_text: str = request.text

    sentence_len = score_ai_detection(user_text)

    return {
        "ai_score": sentence_len,
        "explanation": "The Above is the sentence length"
    }


