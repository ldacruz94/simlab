
from fastapi import APIRouter
from db.models import RunRequestDTO, RunResponseDTO
from service.simulation_service import create_run, get_simulation_run

router = APIRouter()

@router.post("/runs", status_code=201)
async def submit_run(run_request: RunRequestDTO):
    return await create_run(run_request)

@router.get("/runs/{id}", response_model=RunResponseDTO)
async def get_run(id: int):
    return await get_simulation_run(id)
