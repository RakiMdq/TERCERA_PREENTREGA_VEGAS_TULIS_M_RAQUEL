from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def saludar(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_html(request):
    contexto= {
        "profesor":"Juan",
        "ayudantes":["Pipo","Pepa"],
        "comision":522,

    }
    http_response = render(
        request=request,
        template_name='home.html',
        context=contexto,
    )
    return http_response

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response
