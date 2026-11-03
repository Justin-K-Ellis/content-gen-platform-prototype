from pydantic import BaseModel
import yaml
from .config import config


class Prompts(BaseModel):
    RA: str


def get_prompts() -> Prompts:
    try:
        with open(config.raw_prompts) as f:
            data = yaml.safe_load(f)
            print("=== yaml data ===")
            print(data)
        prompts = Prompts(RA=data["RA"])
        return prompts
    except FileNotFoundError as e:
        print(str(e))
        raise FileNotFoundError(f"{config.raw_prompts} could not be found.")
    except Exception as e:
        print(e)
        raise Exception(
            "Unknown error occured when trying to open the raw prompt file."
        )
