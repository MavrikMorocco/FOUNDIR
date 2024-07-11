# image_processor/urls.py
from django.urls import path
from .views import process_image

urlpatterns = [
    path('process/<str:image_path>/', process_image, name='process_image'),
]
