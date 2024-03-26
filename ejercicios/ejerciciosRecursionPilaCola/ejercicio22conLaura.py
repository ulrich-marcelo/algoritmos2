#Busqueda binaria, dado vector ordenado, buscar elemento.

def busquedaBinaria(lista,n):
    if len(lista)==1:
        return lista[0]==n
    elif len(lista)==0:
        return False
    else:
        mid = len(lista)//2
        if n==lista[mid]:
            return True
        elif n < lista[mid]:
            return busquedaBinaria(lista[:mid],n)
        else:
            return busquedaBinaria(lista[mid:],n)
print(busquedaBinaria([1,2,3,4,5,6,7,8,9,10,11,12,22,25,27,33],13))









