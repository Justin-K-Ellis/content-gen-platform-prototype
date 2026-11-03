from pydantic import BaseModel


class Config(BaseModel):
    raw_prompts: str = "app/assets/prompts.yaml"


config = Config()
