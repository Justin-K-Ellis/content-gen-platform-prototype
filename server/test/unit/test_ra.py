from app.providers.ollama import OllamaProvider
from app.utils.dependencies import get_prompts
from db.models.ra import RA


class TestRA:
    prompts = get_prompts()
    llm = OllamaProvider(sys_prompt=prompts.RA)

    def test_get_ra(self):
        item = self.llm.get_ra("Give me an RA item.")
        assert isinstance(item, RA)
