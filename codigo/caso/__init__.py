#! /usr/bin/python
# -*- coding: utf-8 -*-
import altas
import listado
import datos

excepcion = True
while excepcion:
    excepcion = False
    try:
        alumnos = raw_input("Número de alumnos:")
        alumnos = int(alumnos)
        print
    except TypeError, error:
        print error
        excepcion = True
    except ValueError, error:
        print error
        excepcion = True
for iteracion in range(alumnos):
    print "\nAlumno nuevo", iteracion + 1
    nuevo_alumno = altas.alta()
    datos.alumnos.append(nuevo_alumno)

print ("Quihubo")

listado.lista()
