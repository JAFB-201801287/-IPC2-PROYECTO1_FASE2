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
                    request.session["user"] = user.id_usuario
                    return redirect('/cliente/inicio/')
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

def inicio(request):
    id_usuario = request.session['user']
    user = Usuario.objects.get(id_usuario=id_usuario)
    titulo_pantalla = f"CUENTAS DEL USUARIO NO. { str( user.id_usuario ) }"
    cuentas = Cuenta.objects.all().filter(id_usuario= user.id_usuario)
    transacciones = Transaccion.objects.select_related('id_cuenta').all() # devuelve una lista

    if not cuentas:
        print("NO HAY CUENTAS")
    variables = {
        "titulo" : titulo_pantalla,
        "cuentas": cuentas,
        "transacciones": transacciones,
        "user": user
    }
    return render(request, 'cliente/inicio/index.html', variables)

def deposito(request):
    id_usuario = request.session['user']

    form = transaccion()
    form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')

    titulo_pantalla = "DEPOSITO MONETARIO EN CUENTA"
    texto_boton = "ACEPTAR"
    regresar = 'cliente_inicio'

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
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario)
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
        else:
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario)
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'cliente/formulario/index.html', variables)

def activar_cuenta(request):
    id_usuario = request.session['user']

    form = estado()
    form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='SUSPENDIDA')

    titulo_pantalla = "ACTIVAR CUENTA"
    texto_boton = "ACEPTAR"
    regresar = 'cliente_inicio'

    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form
    }

    if (request.method == "POST"):
        form = estado(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            cuenta = datos.get("cuenta")

            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Transaccion(monto, monto_anterior, monto_despues, tipo_moneda, tipo_transaccion, id_cuenta) VALUES('0', '" + str(cuenta.monto) + "', '" + str(cuenta.monto) + "', '" + cuenta.tipo_moneda + "', 'ACTIVAR CUENTA', '" + str(cuenta.id_cuenta) +"');"
            c.execute(consulta)
            db.commit()
            c.close()

            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "UPDATE Cuenta SET estado = 'ACTIVA' WHERE id_cuenta = '" + str(cuenta.id_cuenta) + "';"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()

            form = estado()
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='SUSPENDIDA')
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
        else:
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='SUSPENDIDA')
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'cliente/formulario/index.html', variables)

def suspender_cuenta(request):
    id_usuario = request.session['user']

    form = estado()
    form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')

    titulo_pantalla = "SUSPENDER CUENTA"
    texto_boton = "ACEPTAR"
    regresar = 'cliente_inicio'

    variables = {
        "titulo" : titulo_pantalla,
        "texto_boton": texto_boton,
        "regresar": regresar,
        "form": form
    }

    if (request.method == "POST"):
        form = estado(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            cuenta = datos.get("cuenta")

            host = 'localhost'
            db_name = 'banca_virtual'
            user = 'root'
            contra = 'FloresB566+'
            #puerto = 3306
            #Conexion a base de datos sin uso de modulos
            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "INSERT INTO Transaccion(monto, monto_anterior, monto_despues, tipo_moneda, tipo_transaccion, id_cuenta) VALUES('0', '" + str(cuenta.monto) + "', '" + str(cuenta.monto) + "', '" + cuenta.tipo_moneda + "', 'SUSPENDER CUENTA', '" + str(cuenta.id_cuenta) +"');"
            c.execute(consulta)
            db.commit()
            c.close()

            db = MySQLdb.connect(host=host, user= user, password=contra, db=db_name, connect_timeout=5)
            c = db.cursor()
            consulta = "UPDATE Cuenta SET estado = 'SUSPENDIDA' WHERE id_cuenta = '" + str(cuenta.id_cuenta) + "';"
            c.execute(consulta)
            db.commit()
            c.close()
            #form.save()

            form = estado()
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
        else:
            form.fields['cuenta'].queryset = Cuenta.objects.all().filter(id_usuario=id_usuario).filter(estado='ACTIVA')
            variables = {
                "titulo" : titulo_pantalla,
                "texto_boton": texto_boton,
                "regresar": regresar,
                "form": form
            }
    return render(request, 'cliente/formulario/index.html', variables)