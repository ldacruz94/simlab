"""
db/models.py

Defines the SimulationRun ORM entities and models
"""
from datetime import datetime, UTC
from typing import Any, Dict, List, Optional

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# pylint: disable=missing-class-docstring

class SimulationRun(Base): # pylint: disable=too-few-public-methods
    __tablename__ = "simulation_runs"

    id = Column(Integer, primary_key=True, index=True)
    sim_type = Column(String, nullable=False)
    params = Column(JSON, nullable=False)
    status = Column(String, nullable=False, default="pending")
    submitted_at = Column(DateTime, nullable=False, default=datetime.now(UTC))
    started_at = Column(DateTime, nullable=True)
    finished_at = Column(DateTime, nullable=True)

# DTOs
class RunRequestDTO(BaseModel):
    sim_type: str
    params: Dict[str, Any]

class RunResponseDTO(BaseModel):
    id: int
    sim_type: str
    params: Dict[str, Any]
    status: str
    submitted_at: datetime
    started_at: Optional[datetime]
    finished_at: Optional[datetime]

    model_config = {
        "from_attributes": True
    }

class RunResponseListDTO(BaseModel):
    runs: List[RunResponseDTO]
    total: int
