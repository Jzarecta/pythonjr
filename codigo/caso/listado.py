#! /usr/bin/python
# -*- coding: utf-8 -*-
import datos


def lista():
    numero = 0
    for numero in range(len(datos.alumnos)):
        print "\nalumno: ", numero + 1
        for campo in range(len(datos.alumnos[numero])):
            print datos.campos[0][campo], ": ", datos.alumnos[numero][campo]
