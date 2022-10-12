#Metodo por seleccion
a=[8,7,6,5,4,1]
i=0
for i in range (len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            aux=a[i]
            a[i]=a[j]
            a[j]=aux
print(a)
    
#Si doy vuelta el signo , puedo cambiar de creciente a decreceinte
