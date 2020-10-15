# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:32:53 2019

@author: Alexis Sánchez
"""

class Video:
    #Se define la clase video con los atributos 
    def __init__(self, llave, fecha, titulo, canal, vistas, likes, dislikes, numComments):
        self.llave=llave
        self.fecha=fecha
        self.titulo=titulo
        self.canal=canal
        self.vistas=vistas
        self.likes=likes
        self.dislikes=dislikes
        self.numComments=numComments
        
    def __str__(self):
        cadena="\nDatos del Video"
        cadena+="\Id: "+self.llave
        cadena+="\nFecha: "+self.fecha
        cadena+="\nTitulo: "+self.titulo
        cadena+="\nCanal: "+self.canal
        cadena+="\nVistas: "+self.vistas
        cadena+="\nLikes: "+self.likes
        cadena+="\nDislikes: "+self.dislikes
        cadena+="\nNumero Comentarios: "+self.numComments
        return cadena

import csv

csv_file=open("MXvideos.csv",mode='r', encoding="latin-1") 

lector=csv.reader(csv_file,delimiter=',')
lineas=0
videos=[]
for renglon in lector:
    if lineas==0:
        titulos=""
        for columna in renglon:
            if columna=="video_id":
                titulos+=columna+" "
            if columna=="trending_date":
                titulos+=columna+" "
            if columna=="title":
                titulos+=columna+" "
            if columna=="channel_title":
                titulos+=columna+" "
            if columna=="views":
                titulos+=columna+" "
            if columna=="likes":
                titulos+=columna+" "
            if columna=="dislikes":
                titulos+=columna+" "
            if columna=="comment_count":
                titulos+=columna+" "
        print(titulos.strip())
        lineas+=1
    else:
        info=""
        llave=renglon[0]
        fecha=renglon[1]
        titulo=renglon[2]
        canal=renglon[3]
        vistas=renglon[7]
        likes=renglon[8]
        dislikes=renglon[9]
        numComentarios=renglon[10]
        v=Video(llave,fecha,titulo,canal,vistas,likes,dislikes,numComentarios)
        videos.append(v)

def masLikes(videos):
    mayor=0
    titulo=""
    for i in videos:
        if int(i.likes) > mayor:
            mayor=int(i.likes)
            titulo=i.titulo
    print("El video mas likes es "+titulo+" con un total de "+str(mayor)+" likes")
    
def masDislikes(videos):
    mayor=0
    titulo=""
    for i in videos:
        if int(i.dislikes) > mayor:
            mayor=int(i.dislikes)
            titulo=i.titulo
    print("El video mas dislikes es "+titulo+" con un total de "
          +str(mayor)+" dislikes")
    
def menosLikes(videos):
    menor=int(videos[0].likes)
    titulo=""
    for i in range(1,len(videos)):
        if int(videos[i].likes) < menor and int(videos[i].likes) !=0 :
            menor=int(videos[i].likes)
            titulo=videos[i].titulo
    print("El video menos likes es "+titulo+" con un total de "+str(menor)+" likes")

def menosDislikes(videos):
    menor=int(videos[0].dislikes)
    titulo=""
    for i in range(1,len(videos)):
        if int(videos[i].dislikes) < menor and int(videos[i].dislikes) !=0 :
            menor=int(videos[i].dislikes)
            titulo=videos[i].titulo
    print("El video menos dislikes es "+titulo+" con un total de "
          +str(menor)+" dislikes")

def contienePalabra(palabra):
    s=""
    cont=0
    for i in videos:
        if palabra in i.titulo:
            s+="\n"+i.titulo
            cont+=1
    print("\nVideos que contegan la palabra "+palabra+" :")
    print(s)
    print("Total: "+str(cont))
    
def sumaComentariosPalabras(palabra):
    suma=0
    cont=0
    for i in videos:
        if palabra in i.titulo:
            suma+=int(i.numComments)
            cont+=1
    print("La suma de los comentarios con la palabra "+palabra+" es de: "+str(suma))
    print("Total de videos: "+str(cont))

def contieneDosPalabras(palabra1, palabra2):
    s=""
    cont=0
    for i in videos:
        if palabra1 in i.titulo and palabra2 in i.titulo:
            s+="\n"+i.titulo
            cont+=1
    print("\nVideos que contegan la palabra "+palabra1
          +" y "+palabra2+" :")
    print(s)
    print("Total: "+str(cont))   
    
masLikes(videos)
masDislikes(videos)
menosLikes(videos)
menosDislikes(videos)
contienePalabra("Trump")
contienePalabra("Disney")
#contienePalabra("Chivas")
#contienePalabra("America")
sumaComentariosPalabras("Telenovela")
contieneDosPalabras("Trump", "Mexico")
        
        
        
        
        
