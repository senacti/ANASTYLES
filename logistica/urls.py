from django.http import HttpResponse
from django.shortcuts import render

def logistica_list(request):
    response = HttpResponse("Hola, mundo!")