# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 12:00:19 2019
Implementacion de Grafos
@author: Alexis Sánchez
"""
import networkx as nx
import heapdict as hd
import numpy as np

class Grafo:
    G={}
    visitados={}
    
    def __init__(self):
        self.G={}
        self.visitados={}
    
    def inserta(self,v1,v2,peso=0): #Conecta v1 con v2
        G=self.G
        if v1 not in G:
            G[v1]={}
        if v2 not in G:
            G[v2]={}
        G[v1][v2]=peso
    def insertaSimetrico(self,v1,v2,peso=0):
        self.inserta(v1,v2,peso)
        self.inserta(v2,v1,peso)
    
    def profundidad(self):
        for v1 in G:
            self.visitados[v1]=False
        recorrido=[]
        for v1 in G:
            if not self.visitados[v1]:
                self.dfs(v1,recorrido)
        return recorrido
    
    def dfs(self,v1,recorrido):
        if self.visitados[v1]:
            return
        self.visitados[v1]=True
        recorrido+=[v1]
        for v2 in G[v1]:
            self.dfs(v2,recorrido)
        
    def getGrafo(self):
        G=self.G
        G2={}
        for v1 in G:
            G2[v1]=[]
            for v2 in G[v1]:
                G2[v1]+=[v2]
        return G2
            
    
    def toString(self):
        G=self.G
        for v1 in G:
            for v2 in G[v1]:
                print(str(v1)+" -> "+str(v2)+" peso: "+str(G[v1][v2]))
    def Prim(self,v):
        G=self.G
        visitados=self.visitados
        papa={}
        Q=hd.heapdict()
        for u in G:
            papa[u]=None
            visitados[u]=False
            Q[u]=np.inf
        G[v]=0
        i=0
        l=len(Q)
        while i<l:
            i+=1
            v1, peso=Q.popitem()
            visitados[v1]=True
            for v2 in G[v1]:
                if not visitados[v2] and G[v1][v2]<Q[v2]:
                    papa[v2]=v1
                    Q[v2]=G[v1][v2]
        return papa
                
            
            
    
##Script de prueba    
    
G=Grafo()
G.insertaSimetrico("a","b",4)
G.insertaSimetrico("a","h",8)
G.insertaSimetrico("b","h",11)
G.insertaSimetrico("b","c",8)
G.insertaSimetrico("h","i",7)
G.insertaSimetrico("h","g",1)
G.insertaSimetrico("i","c",2)
G.insertaSimetrico("i","g",6)
G.insertaSimetrico("c","d",7)
G.insertaSimetrico("c","f",4)
G.insertaSimetrico("g","f",2)
G.insertaSimetrico("f","d",14)
G.insertaSimetrico("f","e",10)
G.insertaSimetrico("d","e",9)
G.toString()
G.G
grafo=nx.DiGraph(G.getGrafo())
nx.draw(grafo,with_labels=True)
