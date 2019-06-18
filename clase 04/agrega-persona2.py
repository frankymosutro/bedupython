#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Zona de imports
import click

#Zona de variables
SALIDA = "click-personas.csv"


# @click.command()
# @click.option("-n", type=int, help  = "Remite el mensaje N veces")
# @click.argument("fulano")
# def hola_click(n,fulano):
#     """ESCRIBE UN MENSAJE EN LA SALIDA ESTANDA A FULANO"""
#     for i in range(n):
#      print("HOLA {}!".format(fulano))
 
@click.command()
@click.argument("nombre")
@click.argument("edad", type=int)     
def agrega_persona(nombre, edad):
     """AGREGA UNA PERSONA AL ARCHIVO click-perosnas.cvs"""
#controlador
def main(nombre, edad):
    """funcion principal del script"""
    da = open(SALIDA, "a") #regresa un descriptor de archivo
    da.write("{},{}\n".format(nombre, edad))
    da.close()
    print("se agrego el regitro satisfactoriamente {} al archivo {}".format("{},{}" .format(nombre, edad), SALIDA))
    
        
###todo inicia aqui
if __name__ == "__main__":
    agrega_persona()