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
    regresar = 'admistrador_cliente'
    variables = {
        "titulo" : titulo_pantalla,
        "regresar": regresar,
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
            #form.save()
            form = cliente()
            variables = {
                "titulo" : titulo_pantalla,
                "regresar": regresar,
                "form": form
            }
        else:
            nombre= "INFORMACION INVALIDA"
            variables = {
                "titulo" : titulo_pantalla,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'administrador/agregar.html', variables)

def lista_empresa(request):
    titulo_pantalla = "CLIENTES EMPRESARIALES"
    a = Empresa.objects.all().values_list()  # devuelve una lista

    if not a:
        print("NO HAY EMPRESAS")
    variables = {
        "titulo" : titulo_pantalla,
        "lista": a
    }
    return render(request, 'administrador/empresa/index.html',variables)

def agregar_empresa(request):
    form = empresa()
    titulo_pantalla = "AGREGAR NUEVO CLIENTE EMPRESARIAL"
    regresar = 'admistrador_empresa'
    variables = {
        "titulo" : titulo_pantalla,
        "regresar": regresar,
        "form": form
    }
    if (request.method == "POST"):
        form = empresa(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            nombre_usuario = datos.get("nombre_usuario")
            contrasena = datos.get("contrasena")
            nombre = datos.get("nombre")
            nombre_comercial = datos.get("nombre_comercial")
            nombre_representante = datos.get("nombre_representante")
            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Empresa(nombre, nombre_comercial, nombre_representante) VALUES('" + nombre + "', '" + nombre_comercial + "', '" + nombre_representante + "');"
            c.execute(consulta)
            db.commit()
            c.close()
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            id_empresa = Empresa.objects.last().id_empresa
            consulta = "INSERT INTO Usuario(nombre, contrasena, id_empresa) VALUES('" + nombre_usuario + "', '" + contrasena + "', '" + str(id_empresa) + "');"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()
            form = empresa()
            variables = {
                "titulo" : titulo_pantalla,
                "regresar": regresar,
                "form": form
            }
        else:
            nombre= "INFORMACION INVALIDA"
            variables = {
                "titulo" : titulo_pantalla,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'administrador/agregar.html', variables)

def agregar_cuenta(request):
    form = cuenta()
    titulo_pantalla = "ABRIR CUENTA PARA CLIENTE"
    regresar = 'admistrador_empresa'
    variables = {
        "titulo" : titulo_pantalla,
        "regresar": regresar,
        "form": form
    }
    if (request.method == "POST"):
        form = cuenta(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            monto = datos.get("monto")
            tipo_cuenta = datos.get("tipo_cuenta")
            tipo_moneda = datos.get("tipo_moneda")
            id_usuario = datos.get("usuario")
            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Cuenta(monto, tipo_cuenta, tipo_moneda, id_usuario) VALUES('" + str(monto) + "', '" + tipo_cuenta + "', '" + tipo_moneda + "', '" + str(id_usuario) + "');"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()
            form = cuenta()
            variables = {
                "titulo" : titulo_pantalla,
                "regresar": regresar,
                "form": form
            }
        else:
            variables = {
                "titulo" : titulo_pantalla,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'administrador/agregar.html', variables)