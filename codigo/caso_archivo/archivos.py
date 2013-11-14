#! /usr/bin/python
# -*- coding: utf-8 -*-


def carga_datos(ruta):
    data = []
    with open(ruta, "r") as archivo:
        lineas = archivo.readlines()
    for linea in lineas:
        dato = eval(linea)
        data.append(dato)
    return data
