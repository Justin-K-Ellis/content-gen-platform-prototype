from fastapi import APIRouter, HTTPException, status
from app.providers.ollama import OllamaProvider
from pydantic import BaseModel


class BasicQuery(BaseModel):
    question: str


class BasicAnswer(BasicQuery):
    answer: str


controller = APIRouter(prefix="/ollama")


@controller.post("/", response_model=BasicAnswer, status_code=200)
def query_model(query: BasicQuery) -> BasicAnswer:
    llm = OllamaProvider()
    try:
        res = llm.query(response_model=BasicAnswer, user_prompt=query.question)
        if res is None:
            raise HTTPException(
                detail="LLM could not complete the answer.",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return BasicAnswer(question=query.question, answer=(res))
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
