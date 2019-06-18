#!/usr/bin/env python
#-*- coding: utf-8 -*-

p1 = 6000
p2 = 3000
p3 = 1000
total = p1+p2+p3
print("-"*79)
print("{:40} | {:6}".format("Productos", "Precio"))
print("-"*79)
print("{:40} | {:>10.2f}".format("Lap", p1,))
print("{:40} | {:10.2f}".format("pantalla", p2))
print("{:40} | {:10.2f}".format("pila", p3))
print("-"*79)
print("{:>40} | {:10.2f}".format("Total =", total ))


if -5 > 0:
    print("verdadero")