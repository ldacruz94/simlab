from typing import Any, Dict

from pydantic import BaseModel
from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SimulationRun(Base):
    __tablename__ = "simulation_runs"

    id = Column(Integer, primary_key=True, index=True)


# DTOs
class RunRequestDTO(BaseModel):
    sim_type: str
    params: Dict[str, Any]

class RunResponseDTO(BaseModel):
    id: int
    sim_type: str
    params: Dict[str, Any]