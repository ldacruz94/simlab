
"""
Celery app initialization and task route config
"""

import os

from celery import Celery

celery_app = Celery(
    "simlab",
    broker=os.getenv("RABBITMQ_URL"),
    backend=os.getenv("CELERY_RESULT_BACKEND")
)

celery_app.conf.task_routes = {
    "simlab.tasks.simulation_tasks.run_simulation": {"queue": "simulation_queue"},
}
