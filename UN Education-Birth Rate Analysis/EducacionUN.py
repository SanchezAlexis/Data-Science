# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:56:14 2019
Analisis de la Educacion en Mexico
Datos de Unicef
@author: Alexis Sánchez
"""

class Dato:
    
    def __init__(self, pais,año, informacion, valor):
        self.pais=pais
        self.año=año
        self.informacion=informacion
        self.valor=valor
    
    def __str__(self):
        cadena="\nDato Educativo: "
        cadena+="\nPais: "+self.pais
        cadena+="\nAño: "+self.año
        cadena+="\nInformacion: "+self.informacion
        cadena+="\nValor: "+self.valor
        
        return cadena
    
import csv

def leeArchivoPais(nombreArch,pais):
    csv_file=open(nombreArch,mode='r', encoding="latin-1") 

    lector=csv.reader(csv_file,delimiter=',')
    lineas=0
    datos=[]
    for renglon in lector:
        if lineas==0:
            titulos=""
            for columna in renglon:
                titulos+=columna+" "
            print(titulos.strip())
            lineas+=1
        else:
            p=renglon[1]
            
            if p == pais:
                ps=renglon[1]
                año=renglon[2]
                info=renglon[3]
                valor=renglon[4]
                dato=Dato(ps,año,info,valor)
                datos.append(dato)
    return datos

def imprimeLista(lista):
    for x in lista:
        print(x)
        
def datosAño(año,lista):
    s=""
    if isinstance(lista,Dato):
        for x in lista:
            if int(x.año)==año:
                s+=x.__str__()
        print(s)
        
#mexico=leeArchivoPais("SYB62_T07_Education.csv","Mexico")  
canada=leeArchivoPais("SYB62_T07_Education.csv","Canada")  
imprimeLista(canada)

