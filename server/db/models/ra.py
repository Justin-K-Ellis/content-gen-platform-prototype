from db.models.options import FourOptions
import uuid
from sqlmodel import SQLModel, Field


class RABase(SQLModel):
    stem: str
    options: FourOptions
    key: str


class RA(RABase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    public_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=False)


class RAPublic(RABase):
    public_id: uuid.UUID


class RACreate(RABase):
    pass
