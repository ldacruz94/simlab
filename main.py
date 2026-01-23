

from api.routes import router
from fastapi import FastAPI

from db.models import Base
from db.session import engine

app = FastAPI()

Base.metadata.create_all(bind=engine, checkfirst=True)

app.include_router(router)