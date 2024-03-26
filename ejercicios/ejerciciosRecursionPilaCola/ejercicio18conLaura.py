#Definir funcion aplanar: dada una lista de listas de enteros, 
#retorne una lista de enteros que sea la concatenacion de
#las listas originales

def aplanar(listaDeListas):
    listaPlana = []
    def aplanar_interna(listaDeListasInterna,lista_plana):
        if not listaDeListasInterna:
            return lista_plana
        else:
            lista_plana += listaDeListasInterna[0]
            return aplanar_interna(listaDeListasInterna[1:],lista_plana)
    return aplanar_interna(listaDeListas,listaPlana)

def aplanar_de_pila(listaDeListas,listaPlana = []):
    if not listaDeListas:
        return listaPlana
    else:
        listaPlana += listaDeListas[0]
        return aplanar_de_pila(listaDeListas[1:],listaPlana)
    





print(aplanar([[1,2],[2,3],[3,4]]))

print(aplanar_de_pila([[1,2],[2,3],[3,4]]))






