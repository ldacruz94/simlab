from typing import Any, Dict, List

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SimulationRun(Base):
    __tablename__ = "simulation_runs"

    id = Column(Integer, primary_key=True, index=True)
    sim_type = Column(String, nullable=False)
    params = Column(JSON, nullable=False)

# DTOs
class RunRequestDTO(BaseModel):
    sim_type: str
    params: Dict[str, Any]

class RunResponseDTO(BaseModel):
    id: int
    sim_type: str
    params: Dict[str, Any]

    model_config = {
        "from_attributes": True
    }

class RunResponseListDTO(BaseModel):
    runs: List[RunResponseDTO]
    total: int