from pydantic import BaseModel


class Config(BaseModel):
    raw_prompts: str = "../assets/prompts.yaml"


config = Config()
