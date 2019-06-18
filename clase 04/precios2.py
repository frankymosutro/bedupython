#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Zona de imports
import click


#Zona de variables
SALIDA = "precios.csv"


@click.command()
@click.argument("producto")
@click.argument("cantidad", type=int)  
@click.argument("precio", type=float)  
def agrega_producto(producto, cantidad, precio):
    """AGREGA UNA PERSONA AL ARCHIVO precios.cvs"""
     
    da = open(SALIDA, "a") #regresa un descriptor de archivo
    da.write("{},{},{}\n".format(producto, cantidad, precio))
    da.close()
print("se agrego el regitro satisfactoriamente {} al archivo {}".format("{},{},{}") .format(producto, cantidad, precio), SALIDA))
    
###todo inicia aqui
if __name__ == "__main__":
    agrega_producto()