#Definir la funcion cantidad que dada una lista de enteros y 
#un numero n, retorne la cantidad de apariciones del numero
#n en la lista


def cantidad_de_pila(lista,n):
    if not lista:
        return 0
    else:
        acum = lista[0] == n
        return acum + cantidad_de_pila(lista[1:],n)
    
print(cantidad_de_pila([1,2,3,4,4,3,4,2,4,1],4))









