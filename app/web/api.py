from fastapi import APIRouter, Query
from pydantic import BaseModel
from app.chatbot import ask_question

router = APIRouter()

class AskRequest(BaseModel):
    question: str

@router.post("/ask")
def ask_financial_question_post(payload: AskRequest):
    response = ask_question(payload.question)
    return {"answer": response}

@router.get("/ask")
def ask_financial_question_get(question: str = Query(...)):
    response = ask_question(question)
    return {"answer": response}
