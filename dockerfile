# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables for Celery
ENV CELERY_BROKER_URL redis://redis:8000/0
ENV CELERY_RESULT_BACKEND redis://redis:8000/0

# Set environment variables for Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /code/

# Expose port 8000 to the outside world
EXPOSE 8000

# Define the command to run the Django application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "text_extraction_service.wsgi:application"]
