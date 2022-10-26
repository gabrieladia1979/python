lista=[2,3,5,7,12,15,26,35,47,48]
mini,maxi=0,len(lista)-1
dato=12
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
    print("El dato no esta")
else:
    print("El dato esta en la posc:",posc)

