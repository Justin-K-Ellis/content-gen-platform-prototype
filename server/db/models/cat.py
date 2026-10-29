import uuid
from sqlmodel import SQLModel, Field


class CatBase(SQLModel):
    name: str
    color: str


class Cat(CatBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    public_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=False)


class CatPublic(CatBase):
    public_id: uuid.UUID


class CatCreate(CatBase):
    pass
