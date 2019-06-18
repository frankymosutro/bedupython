#/usr/bin/env python
# -*- coding: utf-8 -*-

# almacen-funciones.py

# Imprime una lista de productos incluyendo
# nombre, cantidad, precio, subtotal y un total
# final utilizando listas de diccionarios.
# def es para definir una funcion 
# Modelo
def obtener_producto():
    """ Obtiene la lista de productos """
    # Datos
    productos = [
        {"nombre":'Mesa', "precio":100, "cantidad":3},
        {"nombre":'Mesa mediana', "precio":200, "cantidad":2},
        {"nombre":'Mesa grande', "precio":500, "cantidad":1}
    ]

    return productos

# Vista
def imprimir_productos(productos, total):
    """ Imprime la lista de productos """
    # Imprimir lista de productos
    for p in productos:
        print("{:40} {:10} {:5} {:10}".format(p["nombre"],
            p["precio"], p["cantidad"], p["subtotal"]))
    # Imprimir total
    print(" "* 58 + "{:10}".format(total))

# Controler
def main():
    """ Función principal del script (Controlador) """
    productos = obtener_producto()
    # Calcular subtotal de cada producto
    for p in productos:
        p["subtotal"] = p["precio"]*p["cantidad"]
    # Calcular el total
    total = sum([p["subtotal"] for p in productos])
    imprimir_productos(productos, total)

# Esto permite a un script funcionar como comando y como módulo
if __name__ == "__main__":
    main()
