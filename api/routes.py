
from fastapi import APIRouter
from db.models import RunRequestDTO, RunResponseDTO

router = APIRouter()

@router.post("/runs", response_model=RunResponseDTO)
def submit_run(run_request: RunRequestDTO):
    print(f"{run_request}")

@router.get("/runs/{id}", response_model=RunResponseDTO)
def get_run(id: str):
    print(f"Hello {id}")

