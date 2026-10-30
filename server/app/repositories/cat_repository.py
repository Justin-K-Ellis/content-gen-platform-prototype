from fastapi import Depends
from sqlmodel import Session, select
from db.models.cat import Cat, CatPublic, CatCreate


class CatRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_cats(self) -> list[CatPublic]:
        cat_sequence = self.session.exec(select(Cat)).all()
        cats: list[CatPublic] = [
            CatPublic(name=cat.name, color=cat.color, public_id=cat.public_id)
            for cat in cat_sequence
        ]
        return cats

    def create_cat(self, cat_data: CatCreate) -> CatPublic:
        cat: Cat = Cat.model_validate(cat_data)
        self.session.add(cat)
        self.session.commit()
        self.session.refresh(cat)
        return CatPublic(name=cat.name, color=cat.color, public_id=cat.public_id)
