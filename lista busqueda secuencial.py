"""
Ingresar una serie de valores, y cargar con ellos una lista, máximo 20

Con los valores que sean impares, generar una segunda lista

Ingresar un valor por teclado y buscarlo de manera secuencial en esta segunda lista

Informar en que posición se lo encuentra
"""
lista=[]
lista1=[]
i=0
dato=int(input("Ingresar un numero:"))
while dato!=-1 and len(lista)<20:
    lista.append(dato)
    if lista[i]%2==1:
        lista1.append(dato)
    dato=int(input("Ingresar un numero:"))
    i=i+1
    

b=int(input("Ingrese el valor que quiere buscar:"))
señal,cont,poscision=0,0,0
while señal != 0 and cont<len(lista1):
    
     if b==lista1(cont):
         posicion=cont
         señal=1
     cont=cont+1     
if señal ==0:        
    print("No esta")
if señal ==1:
    print(poscision)
