from django.shortcuts import render, redirect
from .forms import *
import MySQLdb
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request): 
    form = inicio_sesion()
    texto_boton = "INICIAR SESION"
    variables = {
        "texto_boton": texto_boton,
        "form": form
    }
    if (request.method == "POST"):
        form = inicio_sesion(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data

            nombre_usuario = datos.get("nombre_usuario")
            contrasena = datos.get("contrasena")


            try:
                user = Usuario.objects.get(nombre = nombre_usuario)
                if(user.contrasena == contrasena):
                    return redirect('/administrador/cliente/')
                else: 
                    intentos = user.intentos + 1
                    id_usuario = user.id_usuario
                    host = 'localhost'
                    db_name = 'banca_virtual'
                    user = 'root'
                    contra = 'FloresB566+'
                    #puerto = 3306
                    #Conexion a base de datos sin uso de modulos

                    db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
                    c = db.cursor()
                    consulta = "UPDATE Usuario SET intentos = '" + str(intentos) + "' WHERE id_usuario = '" + str(id_usuario)  + "';"
                    c.execute(consulta)
                    db.commit()
                    c.close()
            except ObjectDoesNotExist:
                print('No existe')

            form = inicio_sesion()
            variables = {
                "texto_boton": texto_boton,
                "form": form
            }
        else:
            variables = {
                "texto_boton": texto_boton,
                "form": form
            }
    return render(request, 'cliente/login/index.html', variables)
