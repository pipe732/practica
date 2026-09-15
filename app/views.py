from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Categoria
# Create your views here.

def vista1(request):
    
    return HttpResponse("Hola Mundo desde la Vista 1")

def vista2(request):
    data = {
        'nombre': 'Felipe', 
        'apellido': 'Rodriguez', 
        'edad': 22, 
    }
    return JsonResponse(data)

def vista3(request):
    titulo = 'categoria'
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {
        'titulo': titulo,
        'categorias': categorias
    })