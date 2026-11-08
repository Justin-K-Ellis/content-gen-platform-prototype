from pydantic import BaseModel


class Config(BaseModel):
    raw_prompts: str = "app/assets/prompts.yaml"
    gemma: str = "gemma4:e2b-mlx"
    qwen: str = "qwen3.5:9b"
    llama: str = "llama2-uncensored:7b"


config = Config()
