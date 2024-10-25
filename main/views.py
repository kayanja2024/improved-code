from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .filters import PatientFilter 
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate
from main.forms import DataForm
from main.forms import PatientForm
from .forms import Sign_upForm
from .models import Ambulance

# Create your views here.
# PatientFilter = OrderFilter


def sign_up(request):

    if request.method == 'POST':
        form = Sign_upForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('dashboard')
    else:
        form = Sign_upForm()
    return render(request, 'main/sign_up.html',{"form":form})


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('login')
        else:
            return render(request, 'main/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')




def dashboard(request):
    patients = Patient.objects.all()
    patient_count = patients.count()
    patients_delivered = Patient.objects.filter(status="Delivered")
    patients_operated = Patient.objects.filter(status="Operated")
    pending = Patient.objects.filter(status="Pending")
    pending_count = pending.count()
    operated_count = patients_operated.count()
    delivered_count = patients_delivered.count()
    ambulances = Ambulance.objects.all()
    ambulances_available = Ambulance.objects.filter(occupied=False).count()
    context = {
        'pending_count': pending_count,
        'patient_count': patient_count,
        'delivered_count': delivered_count,
        'ambulances_available':ambulances_available,
        'operated_count':operated_count,
        'ambulances':ambulances
    }
    print(patient_count)
    return render(request, 'main/dashboard.html', context)


def add_patient(request):
    ambulances = Ambulance.objects.filter(occupied=False)
    doctors = Doctor.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        phone_num = request.POST['phone_num']
        patient_relative_name = request.POST['patient_relative_name']
        patient_relative_contact = request.POST['patient_relative_contact']
        address = request.POST['address']
        symptoms = request.POST['symptoms']
        prior_ailments = request.POST['prior_ailments']
        ambulance_num_sent = request.POST['ambulance_num']
        ambulance_num = Ambulance.objects.get(ambulance_number=ambulance_num_sent)
        dob = request.POST['dob']
        status = request.POST['status']
        doctor = request.POST['doctor']
        doctor = Doctor.objects.get(name=doctor)
        print(request.POST)
        patient = Patient.objects.create(
            name = name,
        phone_num = phone_num,
        patient_relative_name = patient_relative_name,
        patient_relative_contact = patient_relative_contact, 
        address = address, 
        symptoms = symptoms, 
        prior_ailments = prior_ailments, 
        ambulance_num = ambulance_num,
        dob = dob, 
        doctor=doctor,
        status = status
        )
        patient.save()

        ambulance = Ambulance.objects.get(ambulance_number=ambulance_num_sent)
        ambulance.occupied = True
        ambulance.save()
        id = patient.id
        return redirect(f"/patient/{id}")
        
    context = {
        'ambulances': ambulances,
        'doctors': doctors
        
    }
    return render(request, 'main/add_patient.html', context)

def patient(request, pk):
    patient = Patient.objects.get(id=pk)
    if request.method == "POST":
        doctor = request.POST['doctor']
        doctor_time = request.POST['doctor_time']
        doctor_notes = request.POST['doctor_notes']
        mobile = request.POST['mobile']
        mobile2 = request.POST['mobile2']
        relativeName = request.POST['relativeName']
        address  = request.POST['location']
        print(doctor_time)
        print(doctor_notes)
        status = request.POST['status']
        doctor = Doctor.objects.get(name=doctor)
        print(doctor)
        patient.phone_num = mobile
        patient.patient_relative_contact = mobile2
        patient.patient_relative_name = relativeName
        patient.address = address
        patient.doctor = doctor
        patient.doctors_visiting_time = doctor_time
        patient.doctors_notes = doctor_notes
        print(patient.doctors_visiting_time)
        print(patient.doctors_notes)
        patient.status = status
        patient.save()
    context = {
        'patient': patient
    }
    return render(request, 'main/patient.html', context)


def patient_list(request):
    patients = Patient.objects.all()

    #filtering
    myFilter = PatientFilter(request.GET, queryset=patients)

    patients = myFilter.qs
    context = {
        'patients': patients,
        'myFilter': myFilter
    }

    return render(request, 'main/patient_list.html', context)


def autocomplete(request):
    if patient in request.GET:
        name = Patient.objects.filter(name__icontains=request.GET.get(patient))
        name = ['js', 'python']
        
        names = list()
        names.append('Shyren')
        print(names)
        for patient_name in name: 
            names.append(patient_name.name)
        return JsonResponse(names, safe=False)
    return render (request, 'main/patient_list.html')


def autosuggest(request):
    query_original = request.GET.get('term')
    queryset = Patient.objects.filter(name__icontains=query_original)
    mylist = []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)

def autodoctor(request):
    query_original = request.GET.get('term')
    queryset = Doctor.objects.filter(name__icontains=query_original)
    mylist = []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)

def info(request):
    return render(request, "main/info.html")




def register(request):
    form = DataForm()

    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form":form}
    return render(request, "main/register.html",context)



def general_form(request):
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect("/register_form")
    context = {"form":form}
    return render(request, "main/register_form.html",context)




# def login_view(request):
#      return render(request, "main/scan.html")



#Client Code for XML-RPC
#import xmlrpc.client

# Connect to the remote server
# server_url = 'http://localhost:8000/xmlrpc/'
# client = xmlrpc.client.ServerProxy(server_url)

# Call a remote procedure
# response = client.some_remote_procedure(arg1, arg2)

# print("Response from server:", response)




#Client Code for JSON-RPC:

# import json
# import requests

# url = 'http://localhost:8000/jsonrpc/'
# headers = {'Content-Type': 'application/json'}

# # Define the JSON-RPC request
# payload = json.dumps({
#     "jsonrpc": "2.0",
#     "method": "some_remote_procedure",
#     "params": ["param1", "param2"],
#     "id": 1
# })

# # Send the request
# response = requests.post(url, headers=headers, data=payload)

# # Parse the response
# result = response.json()
# print("Response:", result)

