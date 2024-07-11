# face_recognizer/urls.py
from django.urls import path
from .views import detect_view, identify_view

urlpatterns = [
    path('detect/<str:image_path>/', detect_view, name='detect'),
    path('identify/<str:image_path>/', identify_view, name='identify'),
]
