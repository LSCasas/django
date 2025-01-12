from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from psicodemic.models import Psychologist
from psicodemic.models import Patient
from psicodemic.models import Appointment



def list_psychologists(request):
    psychologists = Psychologist.objects.all()
    return render(request, 'psicodemic/psychologists_list.html', {'psychologists': psychologists})

def get_psychologist(request, id):  
    psychologist = Psychologist.objects.get(id=id)
    return HttpResponse(f"Psychologist: FirstName -> {psychologist.first_name}, LastName -> {psychologist.last_name}")

def list_patients (request):
    patients = Patient.objects.all()
    return HttpResponse(patients)

def get_patient(request, id):  
    patient = Patient.objects.get(id=id)
    return HttpResponse(f"Patient: FirstName -> {patient.first_name}, LastName -> {patient.last_name}")

def list_Appointments (request):
    appointments = Appointment.objects.all()
    return HttpResponse(appointments)

def get_appointment(request, id):  
    appointment = Appointment.objects.get(id=id)
    return HttpResponse(f"Appointment: Title -> {appointment.title}")
