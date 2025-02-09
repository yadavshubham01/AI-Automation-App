from src.celery_app import celery
from src.services.gpt_service import generate_gpt_response

@celery.task
def process_gpt_task(prompt: str):
  return generate_gpt_response(prompt)