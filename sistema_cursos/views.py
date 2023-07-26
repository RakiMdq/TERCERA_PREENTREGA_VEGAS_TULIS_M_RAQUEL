from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def saludar(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_html(request):
    http_response = render(
        request=request,
        template_name='home.html',
        context={},
    )
    return http_response


