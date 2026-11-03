from ollama import chat
from ollama import ChatResponse
from pydantic import BaseModel
from db.models.ra import RA


class OllamaProvider:
    def __init__(
        self,
        sys_prompt: str = "You are a helpful assistant.",
    ):
        self.sys_prompt = sys_prompt

    def get_ra(self, prompt: str) -> RA:
        result = self.query(response_model=RA, user_prompt=prompt)
        if result is None:
            raise Exception("RA response was None.")
        return RA.model_validate_json(result)

    def query(self, response_model, user_prompt: str):
        response: ChatResponse = chat(
            model="gemma4:e2b-mlx",
            messages=[
                {"role": "system", "content": self.sys_prompt},
                {"role": "user", "content": user_prompt},
            ],
            format=response_model.model_json_schema(),
        )
        return response.message.content
