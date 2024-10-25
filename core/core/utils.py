#import dlib
# import face_recognition as fr
# import numpy as np
# from profiles.models import profile
# import os

# def is_ajax(request):
#     return request.headers.get('x-requested-with') == 'XMLHttpRequest'

# def get_encoded_faces():
#     qs = profile.objects.all()
#     encoded = {}
#     for p in qs:
#         try:
#             #face = fr.load_image_file(p.photo.path)
#             face = fr.load_image_file("static/images")
#             face_encodings = fr.face_encodings(face)
#             if face_encodings:
#                 encoded[p.user.username] = face_encodings[0]
#             else:
#                 print(f"No face found in the image for user {p.user.username}")
#         except Exception as e:
#             print(f"Error encoding face for user {p.user.username}: {e}")

#     return encoded



# def get_encoded_faces():
#     qs = profile.objects.all()
#     encoded = {}
#     base_image_path = 'static/images'

#     for p in qs:
#         try:
#             # Construct the full path to the user's image
#             image_path = os.path.join(base_image_path, f"{p.user.username}.jpg")  # Adjust extension as needed

#             if os.path.exists(image_path):
#                 face = fr.load_image_file(image_path)
#                 face_encodings = fr.face_encodings(face)

#                 if face_encodings:
#                     encoded[p.user.username] = face_encodings[0]
#                 else:
#                     print(f"No face found in the image for user {p.user.username}")
#             else:
#                 print(f"Image file does not exist for user {p.user.username}: {image_path}")
#         except Exception as e:
#             print(f"Error encoding face for user {p.user.username}: {e}")

#     return encoded


# def classify_face(img):
#     faces = get_encoded_faces()
#     faces_encoded = list(faces.values())
#     known_face_names = list(faces.keys())

#     img = fr.load_image_file(img)

#     try:
#         face_locations = fr.face_locations(img)
#         unknown_face_encodings = fr.face_encodings(img, face_locations)
#         face_names = []

#         for face_encoding in unknown_face_encodings:
#             matches = fr.compare_faces(faces_encoded, face_encoding)
#             face_distances = fr.face_distance(faces_encoded, face_encoding)
#             best_match_index = np.argmin(face_distances)

#             if matches[best_match_index]:
#                 name = known_face_names[best_match_index]
#             else:
#                 name = "unknown"
#             face_names.append(name)

#         return face_names[0] if face_names else "No face found"
#     except Exception as e:
#         print(f"Error during face classification: {e}")
#         return False












# def is_ajax(request):
#     return request.headers.get('x-requested-with') == 'XMLHttpRequest'


# def get_encoded_faces():
#     qs = profile.objects.all()

#     encoded = {}
#     for p in qs:
#         encoded= None

#         face = fr.load_image_file(p.photo.path)
#         face_encodings = fr.face_encodings(face)
#         if len(face_encodings) > 0:
#             encoding = face_encodings[0]

#         else:
#             print("No face found in the image")
        
#         if encoding is not None:
#             encoded[p.user.username] = encoding

#     return encoded

# def classify_face(img):
#     faces = get_encoded_faces()
#     faces_encoded = list(faces.values())
#     known_face_names = list(faces.keys())

#     img = fr.load_image_file(img)

#     try:
#         face_locations = fr.face_locations(img)
#         unknown_face_encodings = fr.face_encodings(img, face_locations)
#         face_names = []

#         for face_encoding in unknown_face_encodings:
#             matches = fr.compare_faces(faces_encoded, face_encoding)
#             face_distances = fr.face_distance(faces_encoded, face_encoding, 
#             best_match_index = np.argmin(face_distances))

#             if matches(best_match_index):
#                 name = known_face_names(best_match_index)
#             else:
#                 name = "unknown"
#             face_names.append(name)

#         return face_names[0]
#     except:
#         return False






# image = face_recognition.load_image_file("photos.jpg")
#pimage = face_recognition.load_image_file("static/images.jpg")

# # Find all the faces in the image
# face_locations = face_recognition.face_locations(image)

# # Or maybe find the facial features in the image
# face_landmarks_list = face_recognition.face_landmarks(image)

# # Or you could get face encodings for each face in the image:
# list_of_face_encodings = face_recognition.face_encodings(image)

# # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
# results = face_recognition.compare_faces(known_face_encodings, a_single_unknown_face_encoding)