# face_recognizer/recognizer.py
import face_recognition

def detect_faces(image_path):
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    return face_locations

def identify_faces(image_path, known_face_encodings):
    # Load the image
    unknown_image = face_recognition.load_image_file(image_path)
    # Find face encodings
    unknown_face_encodings = face_recognition.face_encodings(unknown_image)
    
    # Compare faces
    results = []
    for unknown_face_encoding in unknown_face_encodings:
        results.append((unknown_face_encoding, face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)))
    return results
