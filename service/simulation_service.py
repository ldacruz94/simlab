
from fastapi import HTTPException
from db.models import SimulationRun, RunResponseDTO, RunRequestDTO
from db.session import get_db_session


async def create_run(run_request: RunRequestDTO) -> HTTPException | None:
    try:
        with get_db_session() as session:
            new_run = SimulationRun(
                sim_type=run_request.sim_type,
                params=run_request.params,
            )

            session.add(new_run)
            session.commit()
            session.refresh(new_run)
    except Exception as ex:
        print(f"Could not create simulation run: {ex}")
        raise HTTPException(status_code=500, detail="Failed to create simulation run")

async def get_simulation_run(run_id: int) -> RunResponseDTO | HTTPException:
    try:
        with get_db_session() as session:
            result: SimulationRun | None = (
                session.query(SimulationRun)
                .where(SimulationRun.id == run_id)
                .first()
            )

            if not result:
                raise HTTPException(status_code=404, detail="Simulation Run not found")

            return RunResponseDTO.model_validate(result)

    except HTTPException:
        raise
    except Exception as ex:
        print(f"Simulation run not found: {ex}")
        raise HTTPException(status_code=500, detail="Failed to find run")
