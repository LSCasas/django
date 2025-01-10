from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def list_koder(request):
    context = {
        "bootcamp": {"name": "Python", "module": "Django"},
        "koders": [
        {"name": "Benjamin", "generation": "1g", "bootcamp": "Python", "is_active": True},
        {"name": "Luis", "generation": "1g", "bootcamp": "Python", "is_active": True},
        {"name": "Irving", "generation": "1g", "bootcamp": "Python", "is_active": False}
    ]
    }

    template = loader.get_template("bootcamp/templates/list_koders.html")


    return HttpResponse(template.render(context, request))

def get_koder(request, id):
    nombres = ["Juan", "Ana", "Luis", "Maria", "Carlos"]
    
    if 1 <= id <= len(nombres):  
        nombre = nombres[id - 1]  
        return HttpResponse(f"El nombre con ID {id} es: {nombre}")
    else:
        return HttpResponse(f"ID {id} no es válido. Por favor, ingrese un ID entre 1 y {len(nombres)}.")
