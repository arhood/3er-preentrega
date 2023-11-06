from django.shortcuts import render

# Create your views here.
def usuarios (request):
    contexto = {''}
    http_response = render(
        request = request,
        tamplate_name = 'proyecto/usuarios.html',
        context = contexto,
    )
    return http_response

def temas (request):
    contexto = {''}
    http_response = render(
        request = request,
        tamplate_name = 'proyecto/temas.html',
        context = contexto,
    )
    return http_response

def posts (request):
    contexto = {''}
    http_response = render(
        request = request,
        tamplate_name = 'proyecto/posts.html',
        context = contexto,
    )
    return http_response

def inicio (request):
    contexto = {''}
    http_response = render(
        request = request,
        tamplate_name = 'proyecto/base.html',
        context = contexto,
        )
    return http_response