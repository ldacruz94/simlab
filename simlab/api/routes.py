
from fastapi import APIRouter
from simlab.db.models import RunRequestDTO, RunResponseDTO, RunResponseListDTO
from simlab.service.simulation_service import create_run, get_simulation_run, get_simulation_runs

router = APIRouter()

@router.post("/runs", status_code=201)
async def submit_run(run_request: RunRequestDTO):
    return await create_run(run_request)

@router.get("/runs/{id}", response_model=RunResponseDTO)
async def get_run(id: int):
    return await get_simulation_run(id)

@router.get("/runs", response_model=RunResponseListDTO)
async def get_runs():
    return await get_simulation_runs()
