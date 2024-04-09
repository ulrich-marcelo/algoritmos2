#def funcion partes dada list[int] de una lista de listas que sea el conjunto
#de partes

def partes(lista:list[int])-> list[list[int]]:
    listaListas = [[]]
    def partes_interna(lista_interna):
        if len(lista_interna)==1:
            listaListas.append(lista_interna)
        else:
            inicial = lista_interna.pop(0)
            partes_interna(lista_interna)
            for i in listaListas.copy():
                if not inicial in i:
                    listaListas.append([inicial]+i)
            
    partes_interna(lista)
    return listaListas

print(partes([6,2,3,4]))









