"""Inicializar una lista(mes) con 30 valores 0 (cero)
Generar 2 nros aleatorios
El 1ro, entre 1 y 30 (el dia del mes)
El 2do, entre 0 y 1000 (gasto del dia)
Generar 100 parejas de estos numeros
Puede haber mas de un gasto para un mismo dia
Por fin de proceso informar cual fue el dia  de mayor gasto"""
import random
diamax,valmax=0,0
mes=[]
for i in range (30):
    mes.append(0)
print(lista)
for i in range(100):
    dia=random.randint(1,30)
    gasto=random.randint(0,1000)
    mes[dia-1]=mes[dia-1]+gasto
for i in range(30):
    
    
    
