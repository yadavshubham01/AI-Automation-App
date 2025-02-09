from src.celery_app import celery
from src.services.image_service import generate_image

@celery.task
def generate_image_task(prompt:str):
    return generate_image(prompt)