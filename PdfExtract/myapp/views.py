from importlib.metadata import PackageNotFoundError
from django.shortcuts import render

# text_extractor/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .extractor import extract_text_from_file
from .models import ExtractedText
from .task import extract_text_task
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# @csrf_exempt
# def extract_text(request):
#     if request.method == 'POST':
#         file_path = request.POST.get('file_path')
#         print(file_path)
#         if file_path:
#             text = extract_text_from_file(file_path)
#             if text:                
#                 ExtractedText.objects.create(file_path=file_path, extracted_text=text)
#                 result = extract_text_task.delay(file_path)
#                 subject = 'Your task is completed!'
#                 html_message = render_to_string('task_completed_email.html', {'task_id': extract_text_task.request.id})
#                 plain_message = strip_tags(html_message)
#                 from_email = os.environ.get('EMAIL_HOST_USER'),
#                 to_email = 'nikhil@mailinator.com'
#                 send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)
#                 return JsonResponse({'text': text, 'task_id': result.id})
#             else:
#                 return JsonResponse({'error': 'Unsupported file format'}, status=400)
#         else:
#             return JsonResponse({'error': 'File path not provided'}, status=400)
#     else:
#         return JsonResponse({'error': 'Only POST requests supported'}, status=405)

# Other imports...

@csrf_exempt
def extract_text(request):
    if request.method == 'POST':
        file_path = request.POST.get('file_path')
        print(file_path)
        if file_path:
            try:
                text = extract_text_from_file(file_path)
                if text:
                    ExtractedText.objects.create(file_path=file_path, extracted_text=text)
                    result = extract_text_task.delay(file_path)
                    subject = 'Your task is completed!'
                    html_message = render_to_string('task_completed_email.html', {'task_id': extract_text_task.request.id})
                    plain_message = strip_tags(html_message)
                    from_email = os.environ.get('EMAIL_HOST_USER'),
                    to_email = 'nikhil@mailinator.com'
                    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)
                    return JsonResponse({'text': text, 'task_id': result.id})
                else:
                    return JsonResponse({'error': 'Unsupported file format'}, status=400)
            except PackageNotFoundError as e:
                return JsonResponse({'error': str(e)}, status=400)
        else:
            return JsonResponse({'error': 'File path not provided'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests supported'}, status=405)
