from pydantic import BaseModel


class BasicQuery(BaseModel):
    query: str


class BasicAnswer(BasicQuery):
    response: str
