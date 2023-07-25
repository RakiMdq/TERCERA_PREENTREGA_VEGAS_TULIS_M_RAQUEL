from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def saludar(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html


