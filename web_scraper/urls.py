# web_scraper/urls.py
from django.urls import path
from .views import display_images

urlpatterns = [
    path('images/', display_images, name='display_images'),
]
