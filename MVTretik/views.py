
from os import name
from django.http import HttpResponse
from AppProjecto.models import DatosFamilia
from django.template import Template, Context, loader
from datetime import datetime  
from AppProjecto.views import lista_familiares
def index(request):

    

    archivo = open(r"C:\Users\SAI\Desktop\TrabajoDjango1\MVTretik\MVTretik\template\index.html", "r")
    contenido_html = archivo.read()
    archivo.close()

    plantilla = Template(contenido_html)

    contexto = Context()

    documento_a_renderizar = plantilla.render(contexto)

    return HttpResponse(documento_a_renderizar)



