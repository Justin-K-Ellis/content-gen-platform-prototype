import uuid
from typing import Protocol

from sqlmodel import Session, select

from db.models.ra import RA, RACreate, RAPublic


class RARepositoryProtocol(Protocol):
    def save_ra(self, ra: RACreate) -> RA: ...
    def get_by_id(self, public_id: uuid.UUID) -> RAPublic: ...
    def get_all(self) -> list[RAPublic]: ...


class RARepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save_ra(self, ra: RACreate) -> RA:
        ra_item = RA.model_validate(ra)
        self.session.add(ra_item)
        self.session.commit()
        self.session.refresh(ra_item)
        return ra_item

    def get_by_id(self, public_id: uuid.UUID) -> RAPublic:
        statement = select(RA).where(RA.public_id == public_id)
        ra_item = self.session.exec(statement).one()
        return RAPublic.model_validate(ra_item)

    def get_all(self) -> list[RAPublic]:
        ra_items = self.session.exec(select(RA)).all()
        return [RAPublic.model_validate(ra_item) for ra_item in ra_items]
