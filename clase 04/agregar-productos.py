#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Zona de imports
import sys

#Zona de variables
SALIDA = "productos.csv"

#controlador
def main(parametros):
    """funcion principal del script"""
    da = open(SALIDA, "a") #regresa un descriptor de archivo
    da.write("{},{},{}\n".format(*parametros))
    da.close()
    print("se agrego el regitro satisfactoriamente {} al archivo {}".format (parametros, SALIDA))
    
###todo inicia aqui
if __name__ == "__main__":
    main(sys.argv[1:])