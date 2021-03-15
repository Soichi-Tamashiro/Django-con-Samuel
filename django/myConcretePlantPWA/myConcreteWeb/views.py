# from django.shortcuts import render
from django.views.generic import TemplateView
import shutil  # libreria para mover archivos
import os  # libreria para modificar en el sistema
from django.shortcuts import render  # libreria para activar las paginas
from django.template import (
    Template,
    Context,
)  # libreria para mostrar los template y enviar contextos a los html
import sys
import sqlite3
from itertools import chain
from django.shortcuts import redirect  # libreria para redireccionar paginas
from myConcreteREST.models import *

# Create your views here.
MYPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

myLote = ""


def myIndex(request):

    MYPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    con = sqlite3.connect(MYPATH + "/db.sqlite3")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM myConcreteREST_myconcrete_data")
    data_file = cursor.fetchall()
    # try:
    # ultimo_dato = len(data_file) - 1
    # data_file = data_file[ultimo_dato]
    # context = {
    #     "Lote": data_file[1],
    #     "Empresa": data_file[2],
    #     "Fecha": data_file[3].split(" ")[0],
    #     "Hora": data_file[3].split(" ")[1],
    #     "Cantidad": data_file[4],
    #     "T_Producción": data_file[5],
    #     "RUC": data_file[6],
    #     "Cemento": data_file[7],
    #     "Agregado_1": data_file[8],
    #     "Agregado_2": data_file[9],
    #     "Agua": data_file[10],
    #     "Aditivo_1": data_file[11],
    # }
    # print(context)
    #     return render(request, "Index.html", context)
    # except:
    #     context = {
    #         "Lote": "",
    #         "Empresa": "",
    #         "Fecha": "",
    #         "Hora": "",
    #         "Cantidad": "",
    #         "T_Producción": "",
    #         "RUC": "",
    #         "Cemento": "",
    #         "Agregado_1": "",
    #         "Agregado_2": "",
    #         "Agua": "",
    #         "Aditivo_1": "",
    #     }
    #     print(data_file)

    try:
        ultimo_dato = len(data_file) - 1
        data_file = data_file[ultimo_dato]
        horas = []
        lotes = []
        empresas = []
        produccion = []
        col = []
        context = {}
        if request.method == "POST":
            try:
                fecha = request.POST.get("fecha")
                print(fecha)
                dato = myConcrete_Data.objects.filter(fecha=fecha)
                print(dato)
                for i in range(len(dato)):
                    horas.append(dato[i].hora)
                    lotes.append(dato[i].lote)
                    empresas.append(dato[i].empresa)
                    produccion.append(dato[i].cantidad)
                print(horas)
                a = zip(horas, lotes, empresas, produccion)
                lista = list(a)
                for i in range(len(lista)):
                    col.append(list(lista[i]))
                context = {
                    "Lote": data_file[1],
                    "Empresa": data_file[2],
                    "Fecha": data_file[3],
                    "Cantidad": data_file[4],
                    "T_Producción": data_file[5],
                    "RUC": data_file[6],
                    "Cemento": data_file[7],
                    "Agregado_1": data_file[8],
                    "Agregado_2": data_file[9],
                    "Agua": data_file[10],
                    "Aditivo_1": data_file[11],
                    "Hora": data_file[12],
                    "col": col,
                }
            except:
                context = {
                    "Lote": data_file[1],
                    "Empresa": data_file[2],
                    "Fecha": data_file[3],
                    "Cantidad": data_file[4],
                    "T_Producción": data_file[5],
                    "RUC": data_file[6],
                    "Cemento": data_file[7],
                    "Agregado_1": data_file[8],
                    "Agregado_2": data_file[9],
                    "Agua": data_file[10],
                    "Aditivo_1": data_file[11],
                    "Hora": data_file[12],
                    # "col": col,
                }
            # print(col)
    except:
        print("error")
        # ultimo_dato = len(data_file) - 1
        # data_file = data_file[ultimo_dato]
        # context = {
        #     "Lote": data_file[1],
        #     "Empresa": data_file[2],
        #     "Fecha": data_file[3],
        #     "Cantidad": data_file[4],
        #     "T_Producción": data_file[5],
        #     "RUC": data_file[6],
        #     "Cemento": data_file[7],
        #     "Agregado_1": data_file[8],
        #     "Agregado_2": data_file[9],
        #     "Agua": data_file[10],
        #     "Aditivo_1": data_file[11],
        #     "Hora": data_file[12],
        #     # "col": col,
        # }
        # print(context)
    return render(request, "Index.html", context)
