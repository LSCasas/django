from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from bootcamp.models import Koder
def list_koder(request):
    koders = Koder.objects.all()
    return HttpResponse(koders)

    # context = {
    #     "bootcamp": {"name": "Python", "module": "Django"},
    #     "koders": [
    #     {"name": "Benjamin", "generation": "1g", "bootcamp": "Python", "is_active": True},
    #     {"name": "Luis", "generation": "1g", "bootcamp": "Python", "is_active": True},
    #     {"name": "Irving", "generation": "1g", "bootcamp": "Python", "is_active": False}
    # ]
    # }
    # template = loader.get_template("templates/list_koders.html")


def get_koder(request, id):  
    koder = Koder.objects.get(id=id)
    return HttpResponse(f"Koder: FirstName -> {koder.first_name}, LastName -> {koder.last_name}")