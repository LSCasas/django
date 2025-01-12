from django.urls import path
from .views import list_psychologists, get_psychologist, list_patients, get_patient, list_Appointments, get_appointment

urlpatterns = [
    path("", list_psychologists),  # Listar todos los psicólogos
    path("<int:id>/", get_psychologist),  # Obtener un psicólogo específico
    path("patients/", list_patients),  # Listar todos los pacientes
    path("patients/<int:id>/", get_patient),  # Obtener un paciente específico
    path("appointments/", list_Appointments),  # Listar todas las citas
    path("appointments/<int:id>/", get_appointment),  # Obtener una cita específica
]
