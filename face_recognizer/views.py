# face_recognizer/views.py
from django.shortcuts import render
from .recognizer import detect_faces, identify_faces

def detect_view(request, image_path):
    face_locations = detect_faces(image_path)
    return render(request, 'face_recognizer/detect.html', {'face_locations': face_locations})

def identify_view(request, image_path, known_faces):
    results = identify_faces(image_path, known_faces)
    return render(request, 'face_recognizer/identify.html', {'results': results})
