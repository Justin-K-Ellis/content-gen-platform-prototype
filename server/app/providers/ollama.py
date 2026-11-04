from ollama import chat
from ollama import ChatResponse
from db.models.ra import RA, RACreate
from app.utils.config import config


class OllamaProvider:
    def __init__(
        self,
        sys_prompt: str = "You are a helpful assistant.",
    ):
        self.sys_prompt = sys_prompt

    def gen_ra(self, prompt: str) -> RACreate:
        result = self.query(response_model=RA, user_prompt=prompt)
        if result is None:
            raise Exception("RA response was None.")
        return RACreate.model_validate_json(result)

    def query(self, response_model, user_prompt: str, temp: float = 0.5):
        response: ChatResponse = chat(
            model=config.llama,
            messages=[
                {"role": "system", "content": self.sys_prompt},
                {"role": "user", "content": user_prompt},
            ],
            options={"temperature": temp},
            format=response_model.model_json_schema(),
        )
        return response.message.content
