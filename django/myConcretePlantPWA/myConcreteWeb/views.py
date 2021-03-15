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

    # MYPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # con = sqlite3.connect(MYPATH + "/db.sqlite3")
    # cursor = con.cursor()
    # cursor.execute("SELECT * FROM myConcreteREST_myconcrete_data")
    # data_file = cursor.fetchall()
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
        # ultimo_dato = len(data_file) - 1
        # data_file = data_file[ultimo_dato]
        dato3 = myConcrete_Data.objects.all()
        dato_final = len(dato3) - 1
        # print(dato3)
        context = {
            "Lote": dato3[dato_final].lote,
            "Empresa": dato3[dato_final].empresa,
            "Fecha": dato3[dato_final].fecha,
            "Cantidad": dato3[dato_final].cantidad,
            "T_Producción": dato3[dato_final].t_producción,
            "RUC": dato3[dato_final].ruc,
            "Cemento": dato3[dato_final].cemento,
            "Agregado_1": dato3[dato_final].agregado_1,
            "Agregado_2": dato3[dato_final].agregado_2,
            "Agua": dato3[dato_final].agua,
            "Aditivo_1": dato3[dato_final].aditivo_1,
            "Hora": dato3[dato_final].hora,
            # "col": col,
        }
        horas = []
        lotes = []
        empresas = []
        produccion = []
        col = []

        if request.method == "POST":
            context = {}
            try:
                fecha = request.POST.get("fecha")
                lote = request.POST.get("myLote")
                if fecha != None:
                    # print(fecha)
                    dato = myConcrete_Data.objects.filter(fecha=fecha)
                    # print(dato)
                    for i in range(len(dato)):
                        horas.append(dato[i].hora)
                        lotes.append(dato[i].lote)
                        empresas.append(dato[i].empresa)
                        produccion.append(dato[i].cantidad)
                    # print(horas)
                    a = zip(horas, lotes, empresas, produccion)
                    lista = list(a)
                    for i in range(len(lista)):
                        col.append(list(lista[i]))
                    context = {
                        "Lote": dato3[dato_final].lote,
                        "Empresa": dato3[dato_final].empresa,
                        "Fecha": dato3[dato_final].fecha,
                        "Cantidad": dato3[dato_final].cantidad,
                        "T_Producción": dato3[dato_final].t_producción,
                        "RUC": dato3[dato_final].ruc,
                        "Cemento": dato3[dato_final].cemento,
                        "Agregado_1": dato3[dato_final].agregado_1,
                        "Agregado_2": dato3[dato_final].agregado_2,
                        "Agua": dato3[dato_final].agua,
                        "Aditivo_1": dato3[dato_final].aditivo_1,
                        "Hora": dato3[dato_final].hora,
                        "col": col,
                    }
                if lote != None:
                    # print(lote)
                    dato2 = myConcrete_Data.objects.get(lote=lote)
                    context = {
                        "Lote": dato2.lote,
                        "Empresa": dato2.empresa,
                        "Fecha": dato2.fecha,
                        "Cantidad": dato2.cantidad,
                        "T_Producción": dato2.t_producción,
                        "RUC": dato2.ruc,
                        "Cemento": dato2.cemento,
                        "Agregado_1": dato2.agregado_1,
                        "Agregado_2": dato2.agregado_2,
                        "Agua": dato2.agua,
                        "Aditivo_1": dato2.aditivo_1,
                        "Hora": dato2.hora,
                        # "col": col,
                    }
                # print(context)
            except:
                dato3 = myConcrete_Data.objects.all()
                dato_final = len(dato3) - 1
                # print(dato3)
                context = {
                    "Lote": dato3[dato_final].lote,
                    "Empresa": dato3[dato_final].empresa,
                    "Fecha": dato3[dato_final].fecha,
                    "Cantidad": dato3[dato_final].cantidad,
                    "T_Producción": dato3[dato_final].t_producción,
                    "RUC": dato3[dato_final].ruc,
                    "Cemento": dato3[dato_final].cemento,
                    "Agregado_1": dato3[dato_final].agregado_1,
                    "Agregado_2": dato3[dato_final].agregado_2,
                    "Agua": dato3[dato_final].agua,
                    "Aditivo_1": dato3[dato_final].aditivo_1,
                    "Hora": dato3[dato_final].hora,
                    # "col": col,
                }
            # print(col)
    except:
        print("error")
        # ultimo_dato = len(data_file) - 1
        # data_file = data_file[ultimo_dato]
        context = {
            "Lote": "-",
            "Empresa": "-",
            "Fecha": "-",
            "Cantidad": "-",
            "T_Producción": "-",
            "RUC": "-",
            "Cemento": "-",
            "Agregado_1": "-",
            "Agregado_2": "-",
            "Agua": "-",
            "Aditivo_1": "-",
            "Hora": "-",
            # "col": col,
        }
        # print(context)
    return render(request, "Index.html", context)
