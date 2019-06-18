#/usr/bin/env python
# -*- coding: utf-8 -*-


#Definicion de objetos o clases
class Persona():
    """definicion dle objeto persona"""
    def __init__ (self, nombre, cantidad, precio):
        """constructo de la clase persona"""
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio 
        
    @property  
    def subtotal(self):
            """ Calcula el total"""
            return self.precio * self.cantidad
            
    def __str__(self):
     """formatea el objeto persona en STR"""     
     return  "{:10} {:>3} {:>15.2f} {:15.2f} ". format(self.nombre, self.cantidad, self.precio, self.subtotal)  
    
class Alumno(Persona):
    """definicion dle objeto alumno"""
    def __init__ (self, nombre, cantidad, precio):
        """constructo de la clase alumno"""
        super(). __init__(nombre, cantidad, precio)
        self.marca = marca  
        self.modelo = modelo     
     
    def __str__(self):
     """formatea el objeto persona en STR"""     
     return  "{:30} {:>3} {:>10.2f} {:>10.2f} ". format("{} {} {}") .format(self.marca, self.modelo, self.nombre, 
                                                                            self.cantidad, self.precio, self.subtotal)     
#modelo
def obtener_personas():
    """genera lista de personas tipo personas"""
    #Genera una lista de instancias del objeto Persona 
    personas =[
        Persona("Caja chica",5, 100.00),
        Persona("Caja mediana",3, 185.00),
        Persona("Caja grande",1, 299.00)
        ]
    return personas

def obtener_alumnos():
    """genera lista de personas tipo alumnos"""
    #Genera una lista de instancias del objeto Persona 
    alumnos =[
        Alumno("VW Vochon(200)", 1, 10000.00,),
        Alumno("Seat Cordoba (2010)", 1, 185000.00),
        Alumno("Chevrolet Camaro (2018)", 1, 299000.00)
        ]
    return alumnos
#vista
def imprimir_lista(lista):
    """imprime lista en la salida estandart en formato de texto plano"""
    for i in lista:
        print(i)
def imprimir_personas(personas, total):
    """imprime cajas en la salida estandart en formato de texto plano"""
    for p in Persona:
        print(p)
    # Calcular el total    
    print(" " *31 + "{:>10.2f}".format(total))    
#controlador

def main ():
    """ funcion principal de script"""
    #aplicacion de herencia de clases
    personas = obtener_personas()
    alumnos = obtener_alumnos()
    
    #aplicacion de polimorfismo de clases
    imprimir_lista(personas)
    imprimir_lista(alumnos)
    total = sum([p.subtotal for p in personas])
    imprimir_personas(personas, total)
if __name__ == "__main__":
     main()