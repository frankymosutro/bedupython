#/usr/bin/env python
# -*- coding: utf-8 -*-


#Definicion de objetos o clases
class Cajas():
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
            
    def __str__ (self):
     """formatea el objeto persona en STR"""     
     return  "{:15} {:>3} {:>10.2f} {:>10.2f}".format(self.nombre, self.cantidad, self.precio, self.subtotal)  
    
    
#modelo
def obtener_cajas():
    """genera lista de cajas tipo cajas"""
    #Genera una lista de instancias del objeto Persona 
    cajas =[
        Cajas("caja chica",5, 100.00),
        Cajas("caja mediana", 3, 185.00),
        Cajas("caja grande", 4, 180.00)
        ]
    return cajas
#vista
def imprimir_cajas(cajas, total):
    """imprime cajas en la salida estandart en formato de texto plano"""
    for p in cajas:
        print(p)
    # Calcular el total    
    print(" " *31 + "{:>10.2f}".format(total))

#controlador

def main ():
    """ funcion principal de script"""
    cajas = obtener_cajas()
        
     # Calcular el total
    total = sum([p.subtotal for p in cajas])
    imprimir_cajas(cajas, total)
 
    

if __name__ == "__main__":
     main()