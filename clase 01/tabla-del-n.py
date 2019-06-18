#!/usr/bin/env python
#-*- coding: utf-8 -*-

n = input ("numero: ")
n = int (n)

for i in range(1,11):
    print("{} x {} = {}".format(n, i , n*i))


# numero = input ("numero: ")
#   rango=range(1,11):
#   for elemento in rango:
#      producto= numero*elemento
#      print(numero,  "x", elemento,"=", producto)