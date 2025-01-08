from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def bienvenida(request):
    return HttpResponse("Bienvenido")

def despedida(request):
    return HttpResponse("Despedida")

def saludo(request):
    return HttpResponse("Saludo")

def saludar_con_nombre(request, nombre):
    print("Imrpimiendo..", nombre)
    return HttpResponse(f"Hola {nombre}")

def kodemia(request, nombre):
    if nombre == "mentor":
        return HttpResponse("Hello mentor, here are your classes")
    elif nombre == "koder":
        return HttpResponse("Hello koder, welcome to kodemia")
    else:
        return HttpResponse("You are not welcome here")