from pydantic import BaseModel


class Config(BaseModel):
    prompt_dir: str = "../assets/prompts.yaml"


config = Config()
