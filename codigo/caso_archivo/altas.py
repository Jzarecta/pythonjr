#! /usr/bin/python
# -*-coding: utf-8 -*-
import datos
import valida


def alta():
    """Realiza las altas."""
    alumno_nuevo = []
    contador = 0
    for campo in datos.campos[0]:
        valida_tipo = False
        valida_casos = False
        excepcion = False
        while not (valida_tipo and valida_casos and excepcion):
            excepcion = True
            valida_tipo = True
            valida_casos = True
            mensaje = "Ingrese " + campo + ": "
            valor = raw_input(mensaje)
            if datos.campos[1][contador] != str:
                try:
                    valor = eval(valor)
                    if datos.campos[1][contador] == float and \
                    type(valor) == int:
                        valor = float(valor)
                except:
                    excepcion = False
            valida_tipo = valida.es_el_tipo(valor, datos.campos[1][contador])
            if not valida_tipo:
                continue
            valida_casos = valida.casos_especiales(valor, contador)
            if not valida_casos:
                continue
        contador = contador + 1
        alumno_nuevo.append(valor)
    return alumno_nuevo
