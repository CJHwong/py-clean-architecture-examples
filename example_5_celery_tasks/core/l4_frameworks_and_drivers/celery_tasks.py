from celery_config import app as celery_app
from core.l4_frameworks_and_drivers.celery_dependencies import create_process_data_use_case


@celery_app.task(bind=True, name="process_data_task")
def process_data_task(self, payload: dict):
    """
    This is the Celery task that acts as a bridge to the clean architecture use case.
    """
    use_case = create_process_data_use_case()
    result = use_case.execute(task_id=self.request.id, payload=payload)
    return result
