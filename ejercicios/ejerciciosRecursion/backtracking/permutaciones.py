'''Definir la función permutaciones, que dada una lista de enteros, 
retorne una lista de listas de enteros, donde cada lista es cada 
una de las posibles permutaciones de la lista original.

Por ejemplo: permutaciones([6,2,3]) = 
[[6,2,3], [6,3,2], [2,3,6], [2,6,3], [3,2,6], [3,6,2]]

'''

'''Para cada uno, agarro la lista original sin el elemento y para cada permutacion de
esa minilista, inserto el elemento origial

listaOriginal
indiceActual = 0
elementoActual = listaOriginal[indiceActual]
listaPermutaciones = []
while indiceActual < len(listaOriginal):
    listaCopia = listaOriginal.copy()
    listaCopia.pop(indiceActual)
    permutacionesPrevias = permutaciones(listaCopia)
    for i in permutacionesPrevias:
        i.insert(0,elementoActual)
    listaPermutaciones = listaPermutaciones + permutacionesPrevias






'''


def permutaciones(listaOriginal:list[int])-> list[list[int]]:
    if len(listaOriginal)==1:
        return [listaOriginal]
    else:
        indiceActual = 0
        listaPermutaciones = []
        while indiceActual < len(listaOriginal):
            elementoActual = listaOriginal[indiceActual]
            listaCopia = listaOriginal.copy()
            listaCopia.pop(indiceActual)
            permutacionesPrevias = permutaciones(listaCopia)
            for i in permutacionesPrevias:
                i.insert(0,elementoActual)
            listaPermutaciones = listaPermutaciones + permutacionesPrevias
            indiceActual +=1
        return listaPermutaciones

print(permutaciones([1,2,3,4]))











