import uuid
from sqlmodel import SQLModel, Field, Column
from sqlalchemy import JSON


class RABase(SQLModel):
    stem: str
    options: list[str] = Field(sa_column=Column(JSON))
    key: str


class RA(RABase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    public_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=False)


class RAPublic(RABase):
    public_id: uuid.UUID


class RACreate(RABase):
    pass
