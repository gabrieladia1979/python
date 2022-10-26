"""
Ingresar un valor por el teclado

Determinar si el valor ingresado es un número primo utilizando una función

SI lo es, cargarlo en una lista

Por fin de proceso (-1) informar cuantos valores se agregaron a la lista de primos
""""
def primo(a):
    div,contdiv=1,0
    while div <= a:
        if a%div==0:
            contdiv=contdiv+1
        div=div+1
    if contdiv==2:
        return 1

x=int(input("Ingresar un numero:"))
lista=[]
while x != -1:
    res= primo(x)
    if res ==1:
        lista.append(x)
    x=int(input("Ingresar un numero:"))
print("La cantidad de primos es:",len(lista))
