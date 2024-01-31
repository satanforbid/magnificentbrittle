from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import PatientForm, PersonForm, ProfessionalForm, AssistantForm, RecordForm

def index(request):
    return render(request, 'pages/home.html')
def about_page(request):
    return render(request, 'pages/about.html')
def services_page(request):
    return render(request, 'pages/services.html')
def emergency_page(request):
    return render(request, 'pages/emergency.html')
def login_page(request):
    return render(request, 'pages/login.html')
def signup_page(request):
    return render(request, 'pages/signup.html')
def dashboard_page(request):
    patients = Patients.objects.all()
    return render(request, 'pages/dashboard.html', {'patients':patients})
def profile_page(request, pk):
    patients = Patients.objects.get(id=pk)
    context = {
        "patients":patients,
     }
    return render(request, 'pages/profile.html', context)

def professional_page(request, pk):
    professional = get_object_or_404(Professionals, id=pk)
    context = {
        "professional": professional
    }
    return render(request, 'pages/professionalprofile.html', context)
def assistant_page(request, pk):
    assistant = get_object_or_404(Assistant, id=pk)
    context = {
        "assistant": assistant
    }
    return render(request, 'pages/assistantprofile.html', context)

def records_page(request, patient_id):
    records = get_object_or_404(Records, patient_id=patient_id)
    context = {
        "records": records,
    }
    return render(request, 'pages/records.html', context)
def schedule_page(request):
    return render(request, 'pages/schedule.html')
def createPatientPage(request):
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return redirect('homePage')

    context = {'form': form}
    return render(request, 'pages/patient_form.html', context)
def updatePatient(request, pk):
    patient = get_object_or_404(Patients, id=pk)
    form = PatientForm(instance=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            profile_url = reverse('profilePage', kwargs={'pk': patient.pk})
            return redirect(profile_url)

    context = {'form': form, 'patient': patient}
    return render(request, 'pages/patient_form.html', context)
def deletePatient(request, pk):
    patient = Patients.objects.get(id=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('homePage')
    context = {'patient': patient}
    return render(request, 'pages/delete.html', context)

def createProfessionalPage(request):
    form = ProfessionalForm()
    if request.method == 'POST':
        form = ProfessionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homePage')
    context = {'form':form}
    return render(request, 'pages/professional_form.html', context)

def createAssistantPage(request):
    form = AssistantForm()
    if request.method == 'POST':
        form = AssistantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homePage')
    context = {'form':form}
    return render(request, 'pages/assistant_form.html', context)

def createRecords(request, patient_id):
    patient = get_object_or_404(Patients, id=patient_id)
    form = RecordForm(request.POST or None, initial={'patient': patient})

    if request.method == 'POST' and form.is_valid():
        record = form.save(commit=False)
        record.patient = patient
        record.save()
        return redirect('homePage')

    context = {'form': form, 'patient': patient}
    return render(request, 'pages/records_form.html', context)
def updateRecord(request, records_id):
    records = get_object_or_404(Records, patient_id=records_id)
    form = RecordForm(instance=records)

    if request.method == 'POST':
        form = RecordForm(request.POST, instance=records)
        if form.is_valid():
            form.save()
            records_url = reverse('createRecords')
            return redirect(records_url)

    context = {'form': form, 'records': records}
    return render(request, 'pages/records_form.html', context)
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.user_type == 'P':
                return redirect('profilePage', pk=user.pk)
            if user.user_type == 'M':
                return redirect('professionalPage', pk=user.pk)
            if user.user_type == 'A':
                return redirect('assistantPage', pk=user.pk)
        else:
            # Handle invalid login
            return render(request, 'pages/login.html', {'error': 'Invalid login credentials'})

    # If it's a GET request or authentication failed
    return render(request, 'pages/login.html')





