from django.shortcuts import render, redirect
from .forms import *
import MySQLdb
from django.db.models import Q

# Create your views here.

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

            if((nombre_usuario == 'admin') and (contrasena == 'root1234')):
                return redirect('/administrador/cliente/')

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
    return render(request, 'administrador/login/index.html', variables)

def lista_cliente(request):
    #request.session['a'] = 'HOLA SESION'
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
    texto_boton = "ACEPTAR"
    regresar = 'admistrador_cliente'
    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
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
            consulta = "INSERT INTO Usuario(nombre, contrasena, cui, intentos) VALUES('" + nombre_usuario + "', '" + contrasena + "', '" + str(cui) + "', '0');"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()
            form = cliente()
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
        else:
            nombre= "INFORMACION INVALIDA"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'administrador/formulario.html', variables)

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
    texto_boton = "ACEPTAR"
    regresar = 'admistrador_empresa'
    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
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
            consulta = "INSERT INTO Usuario(nombre, contrasena, id_empresa, intentos) VALUES('" + nombre_usuario + "', '" + contrasena + "', '" + str(id_empresa) + "', '0');"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()
            form = empresa()
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
        else:
            nombre= "INFORMACION INVALIDA"
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'administrador/formulario.html', variables)

def lista_cuenta(request):
    titulo_pantalla = "CLIENTES INDIVIDUALES"
    a = Cuenta.objects.all().values_list()
    u = Usuario.objects.all().values_list() # devuelve una lista
    print(a)

    if not a:
        print("NO HAY CLIENTES")
    variables = {
        "titulo" : titulo_pantalla,
        "lista": a,
        "usuarios": u
    }
    return render(request, 'administrador/cuenta/index.html',variables)

def agregar_cuenta(request):
    form = cuenta()
    titulo_pantalla = "ABRIR CUENTA PARA CLIENTE"
    texto_boton = "ACEPTAR"
    regresar = 'admistrador_cuenta'
    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
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
            usuario = datos.get("usuario")
            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Cuenta(monto, tipo_cuenta, tipo_moneda, id_usuario) VALUES('" + str(monto) + "', '" + tipo_cuenta + "', '" + tipo_moneda + "', '" + str(usuario.id_usuario) + "');"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()
            form = cuenta()
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
        else:
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'administrador/formulario.html', variables)

def deposito(request):
    form = transaccion()
    titulo_pantalla = "DEPOSITO DE MONETARIO EN CUENTA"
    texto_boton = "ACEPTAR"
    regresar = 'admistrador_cuenta'
    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form
    }
    if (request.method == "POST"):
        form = transaccion(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            monto = datos.get("monto")
            tipo_moneda = datos.get("tipo_moneda")
            cuenta = datos.get("cuenta")

            if(cuenta.tipo_moneda == tipo_moneda):
                monto_anterior = cuenta.monto
                monto_despues = (cuenta.monto + monto)
            elif(cuenta.tipo_moneda == 'DOLLAR' and tipo_moneda == 'QUETZAL'):
                monto_anterior = cuenta.monto
                monto_despues = (cuenta.monto + (monto/7.87))
            elif(cuenta.tipo_moneda == 'QUETZAL' and tipo_moneda == 'DOLLAR'):
                monto_anterior = cuenta.monto
                monto_despues = (cuenta.monto + (monto*7.60))

            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Transaccion(monto, monto_anterior, monto_despues, tipo_moneda, tipo_transaccion, id_cuenta) VALUES('" + str(monto) + "', '" + str(monto_anterior) + "', '" + str(monto_despues) + "', '" + tipo_moneda + "', 'DEPOSITO', '" + str(cuenta.id_cuenta) +"');"
            c.execute(consulta)
            db.commit()
            c.close()

            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "UPDATE Cuenta SET monto = '" + str(monto_despues) + "' WHERE id_cuenta = '" + str(cuenta.id_cuenta) + "';"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()
            form = transaccion()
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
        else:
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'administrador/formulario.html', variables)

def agregar_chequera(request):
    form = chequera()
    titulo_pantalla = "CREACION DE CHEQUERA"
    texto_boton = "ACEPTAR"
    regresar = 'admistrador_cuenta'
    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form
    }
    if (request.method == "POST"):
        form = chequera(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            no_cuenta = datos.get("no_cuenta")
            cuenta = Cuenta.objects.get(id_cuenta=no_cuenta)
            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "" #"INSERT INTO Transaccion(monto, monto_anterior, monto_despues, tipo_moneda, tipo_transaccion, id_cuenta) VALUES('" + str(monto) + "', '" + str(monto_anterior) + "', '" + str(monto_despues) + "', '" + tipo_moneda + "', 'DEPOSITO', '" + str(no_cuenta) +"');"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()
            form = transaccion()
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
        else:
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'administrador/formulario.html', variables)