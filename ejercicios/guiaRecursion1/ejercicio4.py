#Definir una función recursiva producto que, dados dos números enteros z y v, retorne
#z*v mediante sumas sucesivas.

def producto_recursivo(z,v):
    if v==1:
        return z
    else:
        return z + producto_recursivo(z,v-1)

#print(producto_recursivo(2,3))
#print(producto_recursivo(3,2))
#print(producto_recursivo(5,4))
