from fastapi import APIRouter, HTTPException, status
from app.providers.ollama import OllamaProvider
from db.models.queries import BasicQuery, BasicAnswer

controller = APIRouter(prefix="/ollama")


@controller.post("/", response_model=BasicAnswer, status_code=200)
def query_model(query: BasicQuery) -> BasicAnswer:
    llm = OllamaProvider()
    try:
        res = llm.query(response_model=BasicAnswer, user_prompt=query.query)
        if res is None:
            raise HTTPException(
                detail="LLM could not complete the answer.",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return BasicAnswer(query=query.query, response=(res))
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
