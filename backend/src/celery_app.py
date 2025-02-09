from celery import Celery

celery=Celery(
    "tasks",
    broker="redis://localhost:6380/0",
    backend="redis://localhost:6380/0"
)

celery.conf.update(task_track_started=True)