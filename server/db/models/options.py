from pydantic import BaseModel


class ThreeOptions(BaseModel):
    A: str
    B: str
    C: str


class FourOptions(ThreeOptions):
    D: str
