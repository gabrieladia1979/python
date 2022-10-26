"""Generar 30 elementos de la serie de Fibonacci, en la lista Fibo

Ingresar un valor desde el teclado y buscarlo en Fibo, por búsqueda binaria

Si está indicar en que posición se lo encuentra

Se recuerda que la serie de Fibonacci comienza con los valores 0 y 1

y que cada elemento se obtiene por la suma de los dos anteriores
"""
def busquedabinaria(lista,dato):
    mini,maxi=0,len(lista)-1
    posc=-1
    while mini<=maxi and posc==-1:
        med=(mini+maxi)//2
        if dato == lista[med]:
            posc=med
        elif dato>lista[med]:
            mini=med+1
        else:
            maxi=med-1

    if posc==-1:
        return("El dato no esta")
    else:
        return("El dato esta en la posc:",posc)

a,b=0,1
lista=[a,b]

for i in range(28):
    c=a+b
    lista.append(c)
    a=b
    b=c
    
print(lista)
print(len(lista))

nro=int(input("Ingresar el numero que desea buscar:"))
print(busquedabinaria(lista,nro))
