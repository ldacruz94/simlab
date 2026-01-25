"""
db/session.py

Contains DB core and configuration
"""
import os
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SESSION_LOCAL = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db_session() -> Generator[Session, None, None]:
    """
    Retrieves DB session
    :return: Session generator
    """
    db = SESSION_LOCAL()
    try:
        yield db
    except SQLAlchemyError as ex:
        print(f"Error connecting: {ex}")
        db.rollback()
    finally:
        db.close()
