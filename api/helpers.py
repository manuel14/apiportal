from . models import *
from django.contrib.auth.models import User, Group
from django.core.files import File
from datetime import datetime
import json


def load_empleados():
    with open('users.json', 'r')as infile:
        data = json.load(infile)
    empleados = []
    for d in data:
        try:
            us = d["email"].split("@")[0]
        except IndexError:
            continue
        emp = Empresa.objects.get(nombre="Tvfuego")
        u = User(username=us, email=d["email"])
        u.set_password(us + "1234")
        u.save()
        e = Empleado(nombre=d["name"], empresa=emp,
                     legajo=d["legajo"], color=d["color"],
                     domicilio=d["domicilio"], user=u)
        empleados.append(e)
    Empleado.objects.bulk_create(empleados)
    return True


def load_empresas():
    with open('empresas.json', 'r')as infile:
        data = json.load(infile)
    empresas = []
    for d in data:
        e = Empresa(nombre=d["nombre"],
                    direccion=d["direccion"], color=d["color"],
                    )
        empresas.append(e)
    Empresa.objects.bulk_create(empresas)
    return True


def load_sectores():
    with open('sectores.json', 'r')as infile:
        data = json.load(infile)
    sectores = []
    for d in data:
        e = Group(name=d["nombre"])
        sectores.append(e)
    Group.objects.bulk_create(sectores)
    return True


def load_recibos(file_path):
    with open('recibos.json', 'r')as infile:
        data = json.load(infile)
    f = File(open(file_path, 'rb'))
    recibos = []
    for r in data:
        emp = Empleado.objects.get(pk=r["empleado"])
        recibo = Recibo(
            periodo=datetime.strptime(r["periodo"], "%d-%m-%Y"),
            empleado=emp,
            archivo=f
        )
        recibos.append(recibo)
    Recibo.objects.bulk_create(recibos)
    return True
