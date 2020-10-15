# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:34:06 2019
Tarea Final
@author: Alexis Sánchez
"""
import pandas as pd
import matplotlib.pyplot as pl

datos2016=pd.read_csv("C:\\Users\Alexis Sánchez\\Documents\\CARPETA ITAM SEMESTRE 3\\DAI\\datosDAI2016.csv",
                 encoding='UTF-8')
datos201701=pd.read_csv("C:\\Users\Alexis Sánchez\\Documents\\CARPETA ITAM SEMESTRE 3\\DAI\\datosDAI201701.csv",
                 encoding='UTF-8')
datos201703=pd.read_csv("C:\\Users\Alexis Sánchez\\Documents\\CARPETA ITAM SEMESTRE 3\\DAI\\datosDAI201703.csv",
                 encoding='UTF-8')
datos2018=pd.read_csv("C:\\Users\Alexis Sánchez\\Documents\\CARPETA ITAM SEMESTRE 3\\DAI\\datosDAI2018.csv",
                 encoding='UTF-8')
datos2019=pd.read_csv("C:\\Users\Alexis Sánchez\\Documents\\CARPETA ITAM SEMESTRE 3\\DAI\\datosDAI2019.csv",
                 encoding='UTF-8')

print("Calificaciones Originales: \n")
print("Datos 2016: \n"+str(datos2016))
print("Datos 2017 Semestre 1: \n"+str(datos201701))
print("Datos 2017 Semestre 1 Grupo 3: \n"+str(datos201703))
print("Datos 2018: \n"+str(datos2018))
print("Datos 2019: \n"+str(datos2019))

def califTot(archivo):
    califTot=archivo['Web']+archivo['Excel']+archivo['Android']
    archivo['Total']=califTot

def normaliza(archivo,porcWeb, porcExcel,porcAndroid):
    archivo['Web']=archivo['Web']*10/(porcWeb/10)
    archivo['Excel']=archivo['Excel']*10/(porcExcel/10)
    archivo['Android']=archivo['Android']*10/(porcAndroid/10)
    
def graficarCursos(archivo):
    h1=archivo.groupby(['Web']).Web.count()
    h2=archivo.groupby(['Excel']).Excel.count()
    h3=archivo.groupby(['Android']).Android.count()
    
    fig1 = pl.figure()
    h1.plot(kind='bar')
    fig1.suptitle('Ponderacion de Calificaciones Web',fontsize=16)
    
    fig2 = pl.figure()
    h2.plot(kind='bar')
    fig2.suptitle('Ponderacion de Calificaciones Excel',fontsize=16)
    
    fig3 = pl.figure()
    h3.plot(kind='bar')
    fig3.suptitle('Ponderacion de Calificaciones Android',fontsize=16)
    
def graficarTotales(archivo):
    h4=archivo.groupby(['Total']).Total.count()
    fig1 = pl.figure()
    h4.plot(kind='bar')
    fig1.suptitle('Ponderacion de Calificaciones Totales',fontsize=16)
    
def promedioTema(archivo):
    frame1=archivo['Web'].mean()
    frame2=archivo['Excel'].mean()
    frame3=archivo['Android'].mean()
    
    print("Promedio de Web: "+str(frame1))
    print("Promedio de Excel: "+str(frame2))
    print("Promedio de Android: "+str(frame3))

def maxMinTema(archivo):
    m1=archivo['Web'].min()
    m2=archivo['Web'].max()
    m3=archivo['Excel'].min()
    m4=archivo['Excel'].max()
    m5=archivo['Android'].min()
    m6=archivo['Android'].max()
    
    print("Calificacion mas baja en Web: "+str(m1))
    print("Calificacion mas alta en Web: "+str(m2))
    print("Calificacion mas baja en Excel: "+str(m3))
    print("Calificacion mas alta en Excel: "+str(m4))
    print("Calificacion mas baja en Android: "+str(m5))
    print("Calificacion mas alta en Android: "+str(m6))
    
def numAlum(archivo):
    n1=archivo['Web'].count()
    print("Numero de alumnos: "+str(n1))

def mayorCalif(archivo,calif):
    datos=0
    f1=archivo['Web']>calif
    frame1=archivo.where(f1)
    num1=frame1['Web'].count()
    datos+=num1
    print("Alumnos con califacion mayor a "+str(calif)+" en Web : "+str(num1))
    f2=archivo['Excel']>calif
    frame2=archivo.where(f2)
    num2=frame2['Web'].count()
    datos+=num2
    print("Alumnos con califacion mayor a "+str(calif)+" en Excel : "+str(num2))
    f3=archivo['Android']>calif
    frame3=archivo.where(f3)
    num3=frame3['Android'].count()
    datos+=num3
    print("Alumnos con califacion mayor a "+str(calif)+" en Android : "+str(num3))
    
    return datos

def cursoMasAlto(archivo):
    proms=[]
    cursos=['Web','Excel','Android']
    n1=archivo['Web'].mean()
    proms.append(n1)
    n2=archivo['Excel'].mean()
    proms.append(n2)
    n3=archivo['Android'].mean()
    proms.append(n3)
    n4=max(proms)
    i=proms.index(n4)
    print("El curso mas alto es "+str(cursos[i]))

califTot(datos2016)
califTot(datos201701)
califTot(datos201703)
califTot(datos2018)
califTot(datos2019)
print("Calificaciones Con Suma Total: \n")
print("Datos 2016: \n"+str(datos2016))
print("Datos 2017 Semestre 1: \n"+str(datos201701))
print("Datos 2017 Semestre 1 Grupo 3: \n"+str(datos201703))
print("Datos 2018: \n"+str(datos2018))
print("Datos 2019: \n"+str(datos2019))

normaliza(datos2016,50,20,30)
normaliza(datos201701,40,25,35)
normaliza(datos201703,40,25,35)
normaliza(datos2018,45,25,30)
normaliza(datos2019,45,25,30)
print("Calificaciones Noramlizadas: \n")
print("Datos 2016: \n"+str(datos2016))
print("Datos 2017 Semestre 1: \n"+str(datos201701))
print("Datos 2017 Semestre 1 Grupo 3: \n"+str(datos201703))
print("Datos 2018: \n"+str(datos2018))
print("Datos 2019: \n"+str(datos2019))

graficarCursos(datos2016)
graficarCursos(datos201701)
graficarCursos(datos201703)
graficarCursos(datos2018)
graficarCursos(datos2019)

graficarTotales(datos2016)
graficarTotales(datos201701)
graficarTotales(datos201703)
graficarTotales(datos2018)
graficarTotales(datos2019)

promedioTema(datos2016)
promedioTema(datos201701)
promedioTema(datos201703)
promedioTema(datos2018)
promedioTema(datos2019)

maxMinTema(datos2016)
maxMinTema(datos201701)
maxMinTema(datos201703)
maxMinTema(datos2018)
maxMinTema(datos2019)

numAlum(datos2016)
numAlum(datos201701)
numAlum(datos201703)
numAlum(datos2018)
numAlum(datos2019)

d1=mayorCalif(datos2016,7)
d2=mayorCalif(datos2016,8)
d3=mayorCalif(datos2016,9)

mayorCalif(datos201701,9)
mayorCalif(datos201701,8)
mayorCalif(datos201701,7)

mayorCalif(datos201701,9)
mayorCalif(datos201703,8)
mayorCalif(datos201703,7)

mayorCalif(datos2018,9)
mayorCalif(datos2018,8)
mayorCalif(datos2018,7)

mayorCalif(datos2019,9)
mayorCalif(datos2019,8)
mayorCalif(datos2019,7)

cursoMasAlto(datos2016)
cursoMasAlto(datos201701)                    
cursoMasAlto(datos201703)
cursoMasAlto(datos2018)
cursoMasAlto(datos2019)

datos2016.hist('Total')

