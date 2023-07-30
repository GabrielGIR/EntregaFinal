from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def inicio(request):
    return render(request, "TerceraPreEntregaRoel/inicio.html")