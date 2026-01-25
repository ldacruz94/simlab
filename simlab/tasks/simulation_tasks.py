
"""
Sim task declarations
"""

from simlab.core.celery_app import celery_app
from simlab.db.models import SimulationRun
from simlab.db.session import get_db_session


@celery_app.task(bind=True, max_retries=3)
def run_simulation(self, run_id: int) -> str | None:
    """
    The celery app run task
    :param self: Celery object
    :param run_id: the sim job run id
    :return: None or error string
    """
    with get_db_session() as session:
        try:
            run: SimulationRun = session.query(SimulationRun).get(run_id)

            if not run:
                return "Run not found"

            run.status = "RUNNING"
            session.commit()

            print(f"Running simulation {run_id} of type {run.sim_type} with params {run.params}")

            run.status = "SUCCEEDED"
            session.commit()
        except LookupError as ex:
            self.retry(exc=ex, countdown=5)
        except Exception as ex: # pylint: disable=broad-exception-caught
            print(f"Simulation {run_id} failed with error: {ex}")
            run.status = "FAILED"
            session.commit()

    return None
