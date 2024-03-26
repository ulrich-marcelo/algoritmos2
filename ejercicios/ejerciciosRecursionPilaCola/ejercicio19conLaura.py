#definir la funcion quicksort: dada lista de enteros, retorna la original pero
#con elementos ordenados. Usar metodo de ordenamiento quicksort.

def quickSort(lista):
    if len(lista)==0:
        return lista
    else:
        vacia = []
        pivote = lista[-1]
        listaIzquierda = [x for x in lista[:-1] if x<pivote]
        listaDerecha = [x for x in lista[:-1] if x>=pivote]
        izquierdaOrdenada = quickSort(listaIzquierda)
        derechaOrdenada = quickSort(listaDerecha)
        vacia += izquierdaOrdenada + [pivote] + derechaOrdenada
        return vacia

print(quickSort([9,2,8,7,2,4,23,4,56,12,2345,2345,245,3]))







