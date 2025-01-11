from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def bienvenida(request):
    return HttpResponse("Bienvenido")

def despedida(request):
    return HttpResponse("Despedida")

def saludo(request):
    return HttpResponse("Saludo")

def saludar_con_nombre(request, nombre):
    context = {
        "name": nombre,
        "lastname": "Perez"
        
        }
    template = loader.get_template("templates/base.html")
    return HttpResponse(template.render(context, request))

def kodemia(request, nombre):
    if nombre == "mentor":
        return HttpResponse("Hello mentor, here are your classes")
    elif nombre == "koder":
        return HttpResponse("Hello koder, welcome to kodemia")
    else:
        return HttpResponse("You are not welcome here")