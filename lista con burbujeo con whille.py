a=[8,7,6,5,4,1]
señal=1
while señal==1:
    señal=0
    for i in range (len(a)-1):
        if a[i]>a[i+1]:
            aux=a[i]
            a[i]=a[i+1]
            a[i+1]=aux
            señal=1
print(a)
