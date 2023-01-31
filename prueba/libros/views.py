from django.shortcuts import render

# Create your views here.
#imports
from django.template import loader
from django.http import HttpResponse


def index(request):
    #Archivo HTML con template
    template = loader.get_template('index.html')
    #logica de la vista
    context = {}
    #respuesta
    return HttpResponse(template.render(context,request))