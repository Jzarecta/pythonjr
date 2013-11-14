#! /usr/bin/python
# -*- coding: utf-8 -*-
import datos
import archivos


def lista_archivo():
    numero = 0
    alumnos = archivos.carga_datos(datos.ruta)
    for numero in range(len(alumnos)):
        print "\nalumno: ", numero + 1
        for campo in range(len(alumnos[numero])):
            print datos.campos[0][campo], ": ", alumnos[numero][campo]
