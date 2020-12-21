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

def agregar_cliente(request):
    form = cliente()
    titulo_pantalla = "AGREGAR NUEVO CLIENTE INDIVIDUAL"
    variables = {
        "titulo" : titulo_pantalla,
        "form": form
    }
    if (request.method == "POST"):
        form = cliente(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            nombre_usuario = datos.get("nombre_usuario")
            contrasena = datos.get("contrasena")
            cui = datos.get("cui")
            nit = datos.get("nit")
            nombre = datos.get("nombre")
            apellido = datos.get("apellido")
            fecha_nacimiento = datos.get("fecha_nacimiento")
            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Cliente(cui, nit, nombre, apellido, fecha_nacimiento) VALUES('" + str(cui) + "', '" + str(nit) + "', '" + nombre + "', '" + apellido +"', '" + fecha_nacimiento + "');"
            c.execute(consulta)
            db.commit()
            c.close()
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Usuario(nombre, contrasena, cui) VALUES('" + nombre_usuario + "', '" + contrasena + "', '" + str(cui) + "');"
            c.execute(consulta)
            db.commit()
            c.close()
            nombre = "Producto registrado de manera correcta"
            #form.save()
            form = cliente()
            variables = {
                "titulo" : titulo_pantalla,
                "form": form
            }
        else:
            nombre= "INFORMACION INVALIDA"
            variables = {
                "titulo" : titulo_pantalla,
                "form": form
            }
    return render(request, 'administrador/agregar.html', variables)