#producto_escalar

def producto_escalar(l1,l2):
    if len(l1)==0:
        if len(l2)==0:
            return 0
        else:
            raise ValueError("Los vectores deben ser del mismo tamaño")
    else:
        prod = l1[0] * l2[0]
        return prod + producto_escalar(l1[1:],l2[1:])


print(producto_escalar([1,2,3],[4,5,6]))








