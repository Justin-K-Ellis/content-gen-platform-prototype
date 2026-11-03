from pydantic import BaseModel
from db.models.options import FourOptions


class RA(BaseModel):
    stem: str
    options: FourOptions
    key: str
