
from simlab.api.routes import router
from fastapi import FastAPI

from simlab.db.models import Base
from simlab.db.session import engine

app = FastAPI()

Base.metadata.create_all(bind=engine, checkfirst=True)

app.include_router(router)