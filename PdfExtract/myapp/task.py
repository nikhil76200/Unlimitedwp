from celery import shared_task
from .extractor import extract_text_from_file

@shared_task
def extract_text_task(file_path):
    return extract_text_from_file(file_path)