from ollama import chat
from ollama import ChatResponse


class OllamaProvider:
    def __init__(self):
        self.sys_prompt = "You are a helpful assistant."

    def query(self, user_prompt: str):
        response: ChatResponse = chat(
            model="gemma4:e2b-mlx",
            messages=[
                {"role": "system", "content": self.sys_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.message.content
