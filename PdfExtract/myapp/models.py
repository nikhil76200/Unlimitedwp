from django.db import models

class ExtractedText(models.Model):
    file_path = models.CharField(max_length=255)
    extracted_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
