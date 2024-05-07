1. Setup project with database with requirements.txt and Virtual environment.
2. Created a .env file to keep database credentials.
3. Makes models for TextExtraction
4. Run Migrations and migrate
5. Created a .gitignore file so that unneccesary and important file will not move to git.
6. Created dockerfile and docker-compose.yml file to explain services used inside this project.
7. Inside myapp make a python file and create function for extract text from docx and pdf.
8. Inside views.py make a function and call extract function.
9. Used Celery to handle multiple user request  simultaneously without blocking.
10. Defines url to run api and get extracted text