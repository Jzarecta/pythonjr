#! /usr/bin/python
# -*- coding: utf-8 -*-
import datos


def es_el_tipo(dato, tipo):
    if tipo not in datos.campos[1]:
        return False
    elif type(dato) == tipo:
        return True
    else:
        return False


def casos_especiales(dato, cuenta):
    if cuenta == 3 and dato not in datos.carreras:
        return False
    if cuenta == 4 and dato < 1:
        return False
    if cuenta == 5 and (dato < 0 or dato > 10):
        return False
    else:
        return True
