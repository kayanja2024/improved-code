# from django.shortcuts import render, redirect
# from django.contrib.auth import logout, login
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from .utils import is_ajax, classify_face
# import base64
# from logs.models import log
# from django.core.files.base import ContentFile
# from django.contrib.auth.models import User
# from profiles.models import profile
# from django.http import HttpResponseBadRequest

# from django.core.files.base import ContentFile
# from django.core.files.storage import default_storage
# from django.http import HttpResponse

# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse
# from PIL import Image
# import cv2
# import os
# import numpy as np



# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# def capture_face():
#     cap = cv2.VideoCapture(0)
#     while True:
#         ret, frame = cap.read()
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
#             roi_gray = gray[y:y+h, x:x+w]
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()
#     return roi_gray  # Return the region of interest (face)




# face_recognizer = cv2.face.LBPHFaceRecognizer_create()

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

# # Train the model with your dataset
# label_map = train_model('static/images')

















# def login_view(request):
#     return render(request, 'scan.html', {})


# def logout_view(request):
#     logout(request)
#     return redirect('/')

# @login_required(login_url='login')
# def home_view(request):
#     return render(request, "main.html", {})

# def find_user_view(request):
#     if is_ajax(request):
#         photo = request.POST.get('photo')
#         _, str_img = photo.split(';base64')
#         decoded_file = base64.b64decode(str_img)

#         x = log()
#         x.photo = ContentFile(decoded_file, 'upload.png')
#         x.photo.save('upload.png', ContentFile(decoded_file))
#         x.save()

#         res = classify_face(x.photo.path)
#         # user_exists = User.objects.filter(usernane=res).exists()
#         user_exists = User.objects.filter(username=res).exists()
#         if user_exists:
#             user = User.objects.get(username=res)
#             profile = profile.objects.get(user=user)
#             x.profile=profile
#             x.save()
#             login(request, user)
#             return redirect('/main/')
#         return JsonResponse({'success':True})        
#     return JsonResponse({'success':False})


# class CustomStorage(FileSystemStorage):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Ensure base_location is a string
#         self.base_location = "your/base/location/path"






# def login_view(request):
#     return render(request, 'scan.html', {})


# def logout_view(request):
#     logout(request)
#     return redirect('/')

# # @login_required(login_url='login')
# def home_view(request):
#     return render(request, "main.html", {})

# def find_user_view(request):
#     if request.method == 'POST':
#         res = request.POST.get('username')
#         user_exists = User.objects.filter(username=res).exists()

#         if user_exists:
#             user = User.objects.get(username=res)
#             profile = user.profile
            
#             # Ensure the photo attribute exists
#             if hasattr(profile, 'photo') and profile.photo:
#                 # Verify image type
#                 try:
#                     with Image.open(profile.photo.path) as img:
#                         if img.mode not in ("L", "RGB"):
#                             return HttpResponse("Unsupported image type, must be 8bit gray or RGB image.", status=400)
#                 except Exception as e:
#                     return HttpResponse(f"Error processing image: {e}", status=400)
            
#             return HttpResponse("User found and image processed.")
#         else:
#             return HttpResponse("User does not exist.", status=404)
#     return HttpResponse("Invalid request method.", status=405)













# def login_view(request):
#     return render(request, 'scan.html', {})

# def logout_view(request):
#     logout(request)
#     return redirect('/')

# @login_required(login_url='login')
# def home_view(request):
#     return render(request, "main.html", {})

# def find_user_view(request):
#     if is_ajax(request):
#         photo = request.POST.get("photo")
#         if photo:
#             try:
#                 _, str_img = photo.split(';base64,')
#                 decoded_file = base64.b64decode(str_img)
                
#                 x = log()
#                 x.photo = ContentFile(decoded_file, "upload.png")
#                 x.photo.save("upload.png", ContentFile(decoded_file))
#                 x.save()
                
#                 res = classify_face(x.photo.path)
#                 user_exists = User.objects.filter(username=res).exists()
#                 if user_exists:
#                     user = User.objects.get(username=res)
#                     user_profile = profile.objects.get(user=user)
#                     x.profile = user_profile
#                     x.save()
#                     login(request, user)
                    
#                     return JsonResponse({'success': True})
#             except Exception as e:
#                 return JsonResponse({'success': False, 'error': str(e)})
#         return JsonResponse({'success': False, 'error': 'Invalid photo format'})

#     return JsonResponse({'success': False, 'error': 'Invalid request'})
#     return render(request, )

# Note: Ensure that your 'classify_face' function returns a valid username if a match is found.
# Also, make sure to handle any exceptions or errors that may occur during file handling and classification.






# def login_view(request):
#     return render(request, 'scan.html', {})


# def logout_view(request):
#     logout(request)
#     return redirect('/')

# @login_required(login_url='login')
# def home_view(request):
#     return render(request, "main.html", {})


# def find_user_view(request):
#     if is_ajax(request):
#         photo = request.POST.get('photo')
#         if not photo:
#             return JsonResponse({'success': False, 'error': 'No photo provided'})

#         try:
#             _, str_img = photo.split(';base64,')
#             decoded_file = base64.b64decode(str_img)

#             x = log()
#             x.photo = ContentFile(decoded_file, 'upload.png')
#             x.photo.save('upload.png', ContentFile(decoded_file))
#             x.save()

#             res = classify_face(x.photo.path)
#             user_exists = User.objects.filter(username=res).exists()
#             if user_exists:
#                 user = User.objects.get(username=res)
#                 user_profile = profile.objects.get(user=user)
#                 x.profile = user_profile
#                 x.save()
#                 login(request, user)
#                 return JsonResponse({'success': True})
#             return JsonResponse({'success': False, 'error': 'User not found'})
#         except Exception as e:
#             return JsonResponse({'success': False, 'error': str(e)})
#     else:
#         return HttpResponseBadRequest('Invalid request type')
    


# def find_user_view(request):
#     if request.method == 'POST':
#         # Assume decoded_file is already defined correctly
#         decoded_file = request.FILES['file'].read()
        
#         # Saving the file
#         file_name = 'upload.png'
#         content_file = ContentFile(decoded_file)
        
#         # Save the file with the default storage (or your custom storage)
#         saved_name = default_storage.save(file_name, content_file)
        
#         # Now save the file name to your model
#         x.photo.name = saved_name
#         x.save()
        
#     return HttpResponse('File uploaded successfully')