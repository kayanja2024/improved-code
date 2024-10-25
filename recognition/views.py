from django.shortcuts import render
from .models import User
from django.core.files.storage import FileSystemStorage
import cv2
import os
import numpy as np
# Create your views here.


# Load the pre-trained face detection model
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Initialize the face recognizer
# face_recognizer = None
# label_map = {}

# if hasattr(cv2, 'face'):
#     face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# else:
#     raise ImportError("The 'face' module is not available in your OpenCV installation.")

# def train_model(data_path):
#     faces = []
#     labels = []
#     label_map = {}
#     current_label = 0

#     for dir_name in os.listdir(data_path):
#         dir_path = os.path.join(data_path, dir_name)
#         if os.path.isdir(dir_path):
#             label_map[current_label] = dir_name
#             for img_name in os.listdir(dir_path):
#                 img_path = os.path.join(dir_path, img_name)
#                 img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
#                 faces.append(img)
#                 labels.append(current_label)
#             current_label += 1

#     faces = np.array(faces)
#     labels = np.array(labels)
#     face_recognizer.train(faces, labels)
#     return label_map

# # Train the model with your dataset (update 'path_to_your_dataset' to your actual dataset path)
# label_map = train_model('static/images')

# def home(request):
#     return render(request, 'recognition/home.html')

# def upload_image(request):
#     if request.method == 'POST':
#         if 'image' not in request.FILES:
#             return render(request, 'recognition/upload.html', {'error': 'No image uploaded.'})

#         uploaded_file = request.FILES['image']
#         fs = FileSystemStorage()
#         filename = fs.save(uploaded_file.name, uploaded_file)
#         file_url = fs.url(filename)

#         # Perform face recognition
#         img = cv2.imread(fs.path(filename), cv2.IMREAD_GRAYSCALE)
#         if img is None:
#             return render(request, 'recognition/upload.html', {'error': 'Failed to read uploaded image.'})

#         label, confidence = face_recognizer.predict(img)
#         user_name = label_map[label]

#         context = {'file_url': file_url, 'user_name': user_name}
#         return render(request, 'recognition/result.html', context)
#     return render(request, 'recognition/upload.html')