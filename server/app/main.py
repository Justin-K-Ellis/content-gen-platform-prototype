from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
import uvicorn
from sqlmodel import Session, select

from db.engine import init_db, get_session
from db.models.cat import Cat, CatCreate, CatPublic
from app.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)


@app.get("/")
def root() -> dict[str, str]:
    return {"msg": "hello app"}


@app.post("/cat", response_model=CatPublic)
def create_cat(
    cat_data: CatCreate, session: Session = Depends(get_session)
) -> CatPublic:
    cat: Cat = Cat.model_validate(cat_data)
    session.add(cat)
    session.commit()
    session.refresh(cat)
    return CatPublic(name=cat.name, color=cat.color, public_id=cat.public_id)


@app.get("/cat", response_model=list[CatPublic])
def get_cats(session: Session = Depends(get_session)) -> list[CatPublic]:
    cat_sequence = session.exec(select(Cat)).all()
    cats: list[CatPublic] = [
        CatPublic(name=cat.name, color=cat.color, public_id=cat.public_id)
        for cat in cat_sequence
    ]
    return cats


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
