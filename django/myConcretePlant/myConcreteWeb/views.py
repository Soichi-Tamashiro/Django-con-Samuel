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

# Create your views here.


def myIndex(request):

    MYPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    con = sqlite3.connect(MYPATH + "/db.sqlite3")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM myConcreteREST_myconcrete_data")
    data_file = cursor.fetchall()
    try:
        ultimo_dato = len(data_file) - 1
        data_file = data_file[ultimo_dato]
        context = {
            "Lote": data_file[2],
            "Empresa": data_file[3],
            "Fecha": data_file[4].split(" ")[1],
            "Hora": data_file[4].split(" ")[0],
            "Cantidad": data_file[5],
            "T_Producción": data_file[6],
            "RUC": data_file[7],
            "Cemento": data_file[8],
            "Agregado_1": data_file[9],
            "Agregado_2": data_file[10],
            "Agua": data_file[11],
            "Aditivo_1": data_file[12],
        }
        print(context)
        return render(request, "Index.html", context)
    except:
        context = {
            "Lote": "",
            "Empresa": "",
            "Fecha": "",
            "Hora": "",
            "Cantidad": "",
            "T_Producción": "",
            "RUC": "",
            "Cemento": "",
            "Agregado_1": "",
            "Agregado_2": "",
            "Agua": "",
            "Aditivo_1": "",
        }
        print(data_file)
        return render(request, "Index.html", context)
