from sqlmodel import SQLModel, Session, create_engine

import db.models  # noqa: F401 — ensures all models are registered before create_all

DATABASE_URL = "sqlite:///./gtec.db"

engine = create_engine(DATABASE_URL, echo=True)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
