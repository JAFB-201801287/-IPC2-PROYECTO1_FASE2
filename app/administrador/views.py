from django.shortcuts import render
from .forms import *
import MySQLdb
from django.db.models import Q

# Create your views here.

def login(request):
    return render(request, 'administrador/login/index.html')

def lista_cliente(request):
    titulo_pantalla = "CLIENTES INDIVIDUALES"
    a = Cliente.objects.all().values_list()  # devuelve una lista
    print(a)

    if not a:
        print("NO HAY CLIENTES")
    variables = {
        "titulo" : titulo_pantalla,
        "lista": a
    }
    return render(request, 'administrador/cliente/index.html',variables)

