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
    
    
#modelo
def obtener_personas():
    """genera lista de personas tipo personas"""
    #Genera una lista de instancias del objeto Persona 
    personas =[
        Persona("PEPE","Lucas",34),
        Persona("Mario","Martinez",15)
        ]
    return personas
#vista
def imprimir_personas(personas):
    """imprime personas en la salida estandart en formato de texto plano"""
    for p in personas:
        print(p)
    
#controlador

def main ():
    """ funcion principal de script"""
    personas = obtener_personas()
    imprimir_personas(personas)

if __name__ == "__main__":
     main()