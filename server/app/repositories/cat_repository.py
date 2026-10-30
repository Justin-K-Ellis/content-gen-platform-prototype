from sqlmodel import Session, select
from db.models.cat import Cat, CatPublic, CatCreate


class CatRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_cats(self) -> list[Cat]:
        cat_sequence = self.session.exec(select(Cat)).all()
        return list(cat_sequence)

    def create_cat(self, cat_data: CatCreate) -> Cat:
        cat: Cat = Cat.model_validate(cat_data)
        self.session.add(cat)
        self.session.commit()
        self.session.refresh(cat)
        return cat
