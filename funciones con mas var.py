#funciones
#2-Funciones con dos variables
"""
print("Hola")
print("Fin")
Esto no, lo querio como funcion
"
def superficie (a,b):
    a=a*2
    b=b*2
    print("a",a)
    print("b",b)
    print("La superficie es:",a*b)

a=5
b=6

superficie(a,b)
print("a",a)
print("b",b)
print("Fin")
Cuando salgo de una funcion, el valor que cambiamos, se perdio y queda el original
del programa principal"""
#La a del prog principal es distinta con la a de la funcion
#Por eso ahora , ahora vamos a usar nombre de var distintas y nos guiamos por posicionamiento

def superficie (x,y):
    sup=x*y
    return sup

a=5
b=6
resultado=superficie(a,b)
print("La superficie es ",resultado)




#ponemos var dist, x e y en funcion y desde la principal llamamos a  a y b como los valores que van a ser x e y
