a=[8,7,6,5,4,1]
for b in range(len(a)-1):
    for i in range (len(a)-1):
            if a[i]>a[i+1]:
                aux=a[i]
                a[i]=a[i+1]
                a[i+1]=aux
print(a)
