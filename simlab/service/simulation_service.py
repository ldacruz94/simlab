
from fastapi import HTTPException
from simlab.db.models import SimulationRun, RunResponseDTO, RunRequestDTO, RunResponseListDTO
from simlab.db.session import get_db_session


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

async def get_simulation_runs() -> RunResponseListDTO:
    try:
        with get_db_session() as session:
            results = session.query(SimulationRun).all()

            if not results:
                raise HTTPException(status_code=404, detail="Simulation Run not found")

            return RunResponseListDTO(
                runs=[RunResponseDTO.model_validate(r) for r in results],
                total=len(results)
            )
    except HTTPException:
        raise
    except Exception as ex:
        print(f"Simulation run not found: {ex}")
        raise HTTPException(status_code=500, detail="Failed to find run")
