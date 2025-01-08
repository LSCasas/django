from django.contrib import admin
from django.urls import path

from .views import list_koder, get_koder

urlpatterns = [
    path("koders/", list_koder),
    path("koders/<int:id>/", get_koder),  
]
