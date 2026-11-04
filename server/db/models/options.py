# from pydantic import BaseModel
from sqlmodel import SQLModel


class ThreeOptions(SQLModel):
    A: str
    B: str
    C: str


class FourOptions(ThreeOptions):
    D: str
