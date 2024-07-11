# image_processor/processing.py
from PIL import Image

def resize_image(image_path, output_path, size=(128, 128)):
    try:
        img = Image.open(image_path)
        img = img.resize(size, Image.ANTIALIAS)
        img.save(output_path)
        return output_path
    except IOError:
        print("Cannot resize the image.")
        return None

def convert_to_grayscale(image_path, output_path):
    try:
        img = Image.open(image_path)
        img = img.convert("L")  # Convert to grayscale
        img.save(output_path)
        return output_path
    except IOError:
        print("Cannot convert the image to grayscale.")
        return None
