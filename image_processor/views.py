# image_processor/views.py
from django.shortcuts import render
from .processing import resize_image, convert_to_grayscale

def process_image(request, image_path):
    resized_path = resize_image(image_path, 'path/to/resized/image.jpg')
    grayscale_path = convert_to_grayscale(image_path, 'path/to/grayscale/image.jpg')
    context = {
        'resized_image': resized_path,
        'grayscale_image': grayscale_path
    }
    return render(request, 'image_processor/process_image.html', context)
