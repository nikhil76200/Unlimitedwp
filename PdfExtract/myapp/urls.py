from django.urls import path
from . import views





urlpatterns = [

   path('extract/', views.extract_text, name='extract_text'),
  
]
