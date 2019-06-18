#/usr/bin/env python
# -*- coding: utf-8 -*-


#Definicion de objetos o clases
class Persona():
    """definicion dle objeto persona"""
    def __init__ (self, nombre, a_paterno, edad):
        """constructo de la clase persona"""
        self.nombre = nombre
        self.a_paterno = a_paterno
        self.edad = edad 
        
    @property  
    def edad_real(self):
            """ Clcula la edad real"""
            return self.edad + 5
            
    def __str__(self):
     """formatea el objeto persona en STR"""     
     return  "{:10} {:15} {:>3} {:>3}". format(self.nombre, self.a_paterno, self.edad, self.edad_real)  
    
class Alumno(Persona):
    """definicion dle objeto alumno"""
    def __init__ (self, nombre, a_paterno, edad, matricula):
        """constructo de la clase alumno"""
        super(). __init__(nombre, a_paterno,edad)
        self.matricula = matricula    
     
    def __str__(self):
     """formatea el objeto persona en STR"""     
     return  "{:10} {:15} {:>3} {:>3} {:5}". format(self.nombre, self.a_paterno, self.edad, self.edad_real, self.matricula)     
#modelo
def obtener_personas():
    """genera lista de personas tipo personas"""
    #Genera una lista de instancias del objeto Persona 
    personas =[
        Persona("PEPE","Lucas",34),
        Persona("Mario","Martinez",15)
        ]
    return personas

def obtener_alumnos():
    """genera lista de personas tipo alumnos"""
    #Genera una lista de instancias del objeto Persona 
    alumnos =[
        Alumno("Jaime","Picac",34, "132465"),
        Alumno("Oscar","Perez",15, "14785")
        ]
    return alumnos
#vista
def imprimir_lista(lista):
    """imprime lista en la salida estandart en formato de texto plano"""
    for i in lista:
        print(i)
    
#controlador

def main ():
    """ funcion principal de script"""
    #aplicacion de herencia de clases
    personas = obtener_personas()
    alumnos = obtener_alumnos()
    
    #aplicacion de polimorfismo de clases
    imprimir_lista(personas)
    imprimir_lista(alumnos)

if __name__ == "__main__":
     main()