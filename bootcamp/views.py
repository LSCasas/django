from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list_koder(request):
    nombres = ["Juan", "Ana", "Luis", "Maria", "Carlos"]
    nombres_str = ""
    
    for i, nombre in enumerate(nombres, start=1):
        nombres_str += f"ID: {i} - Nombre: {nombre}<br>"
    
    return HttpResponse(f"Lista de nombres con ID:<br>{nombres_str}")

def get_koder(request, id):
    nombres = ["Juan", "Ana", "Luis", "Maria", "Carlos"]
    
    if 1 <= id <= len(nombres):  
        nombre = nombres[id - 1]  
        return HttpResponse(f"El nombre con ID {id} es: {nombre}")
    else:
        return HttpResponse(f"ID {id} no es válido. Por favor, ingrese un ID entre 1 y {len(nombres)}.")
