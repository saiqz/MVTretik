from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from AppProjecto.models import DatosFamilia
from django.template import Template, Context, loader



def lista_familiares(request):

    datos = DatosFamilia.objects.all()
    lista_nombre_familiares = []

    for dato in datos:
        lista_nombre_familiares.append(dato.name)

    
    return HttpResponse(lista_nombre_familiares)