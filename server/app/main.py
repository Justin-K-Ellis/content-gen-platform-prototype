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


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
