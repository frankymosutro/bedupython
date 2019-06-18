#!/usr/bin/env python
#-*- coding: utf-8 -*-

es_edad = False
    
while not es_edad:
    num= input( "escribe tu edad :")
    if num.isdigit() and int (num) > 0:
      es_edad = True 

    num = int (num)
    print("Tu edad es :", num)  

