from django.shortcuts import render
from django.http import HttpResponse
#ejecuta las ventas yo elijo que pantalla mostrar

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hola Mundo de POO2 Juank</h1>')

