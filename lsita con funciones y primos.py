"""Cargar una lista con 30 valores aleatorios comprendidos entre 20 y 80
Una funcion determinara si el valor es un numero primo
Si es asi, el valor sera cargado a otra lista
Ordenar esta segunda lista de mayor a menor"""
import random
lista=[]

def primo(nro):
    div,contdiv=1,0
    while nro >= div:
        if nro % div == 0:
            contdiv=contdiv+1
        div=div+1
    if contdiv==2:
        return 1
    else:
        return 0
    
for x in range (30):
    nro=random.randint(20,80)
    primo(nro)
    if primo(nro)==1:
        lista.append(nro)

print("Lista desordenada:",lista)

for b in range(len(lista)-1):
    for i in range (len(lista)-1):
            if lista[i]>lista[i+1]:
                aux=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux
print("Lista ordenada:",lista)

