from typing import Protocol

from sqlmodel import Session, select

from db.models.cat import Cat, CatCreate


class CatRepositoryProtocol(Protocol):
    def get_cats(self) -> list[Cat]: ...
    def create_cat(self, cat_data: CatCreate) -> Cat: ...
    def get_by_name(self, name: str) -> Cat | None: ...


class CatRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_cats(self) -> list[Cat]:
        cat_sequence = self.session.exec(select(Cat)).all()
        return list(cat_sequence)

    def get_by_name(self, name: str) -> Cat | None:
        statement = select(Cat).where(Cat.name == name)
        rows = list(self.session.exec(statement))
        if len(rows) == 0:
            return None
        else:
            return rows[0]

    def create_cat(self, cat_data: CatCreate) -> Cat:
        cat: Cat = Cat.model_validate(cat_data)
        self.session.add(cat)
        self.session.commit()
        self.session.refresh(cat)
        return cat
