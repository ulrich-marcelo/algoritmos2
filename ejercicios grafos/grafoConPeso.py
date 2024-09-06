"""
Conjunto de Nodos y Aristas
Nodos: lista, tupla, etc.
Aristas: lista de tuplas

Implementar Grafo Simple

Se puede crear Grafo Vacio

- agregar_nodo
- agregar arista
- eliminar_nodo
- eliminar_arista
- existe_conexion
- es_vecino_de
- vecinos_de

"""
from typing import Generic, TypeVar, Optional,Union
from functools import reduce
T = TypeVar('T')


class GrafoAdyacencia(Generic[T]):
    def __init__(self, vertices: set[T]=set(),aristas: dict[T , dict[T,int]]= {}) -> None:
        self.vertices = vertices
        self.aristas = aristas

    def agregar_nodo(self,nodo:T) -> None:
        self.vertices.add(nodo)
        self.aristas[nodo] = dict()

    def agregar_arista(self,arista:tuple[T,T],peso:int=0) -> None:
        self.aristas[arista[0]][arista[1]]=peso
        self.aristas[arista[1]][arista[0]]=peso

    def eliminar_nodo(self,nodo:T) -> None:
        self.vertices.discard(nodo)

    # def eliminar_arista(self,arista:tuple[T,T]) -> None:
    #     self.aristas[arista[0]].discard(arista[1])
    #     self.aristas[arista[1]].discard(arista[0])

    def es_vecino_de(self,nodoA:T,nodoB:T) -> bool:
        return nodoB in self.aristas[nodoA]
    
    def vecinos_de(self,nodo:T) -> list[T]:
        return list(self.aristas[nodo].keys())
    
    def __str__(self) -> str:
        return f"Vertices = {self.vertices} \n Aristas = {self.aristas}"
    
    def camino_minimo(self,origen:T,destino:T)->list[T]:
        def init():
            pasadas = dict()
            for nodo in self.vertices:
                if nodo == origen:
                    pasadas[nodo]={"antecesor":None,"costo":0} #seria infinito pero no quiero importar math
                else:
                    pasadas[nodo]={"antecesor":None,"costo":99999999} #seria infinito pero no quiero importar math
            return pasadas
        dict_pasadas = init()
        sin_visitar = list(self.vertices)
        
        def marcar(origen,sin_visitar:list[T]):
            if sin_visitar:
                nodo_minimo = origen
                vecinos = self.vecinos_de(nodo_minimo)
                for vecino in vecinos:
                    if vecino in sin_visitar:        
                        if dict_pasadas[vecino]["costo"] > dict_pasadas[nodo_minimo]["costo"] + self.aristas[nodo_minimo][vecino]:
                            dict_pasadas[vecino]["antecesor"]=nodo_minimo
                            dict_pasadas[vecino]["costo"] = dict_pasadas[nodo_minimo]["costo"] + self.aristas[nodo_minimo][vecino]
                vecino_minimo:T|None = None
                costo_minimo = 99999999999
                for vecino in vecinos:
                    if vecino in sin_visitar:
                        if costo_minimo>dict_pasadas[vecino]["costo"]:
                            vecino_minimo = vecino
                            costo_minimo = dict_pasadas[vecino]["costo"]
                if vecino_minimo is not None:
                    sin_visitar.remove(vecino_minimo)
                    marcar(vecino_minimo,sin_visitar)
        sin_visitar.remove(origen)
        marcar(origen,sin_visitar)

        # def recorrer(origen,destino,recorrido):
        #     vecinos = self.vecinos_de(origen)
        #     vecino_minimo = None
        #     costo_minimo = 999999
        #     for vecino in vecinos:
        #         if vecino not in recorrido:
        #             if dict_pasadas[vecino]["costo"]<costo_minimo:
        #                 vecino_minimo = vecino
        #                 costo_minimo = dict_pasadas[vecino]["costo"]
        #     if vecino_minimo is not None:
        #         recorrido.append(vecino_minimo)
        #     if vecino_minimo!= destino:
        #         recorrer(vecino_minimo,destino,recorrido)

        def recorrer(origen,destino,recorrido):
            if origen != destino:
                siguiente = dict_pasadas[origen]["antecesor"]
                recorrido.append(siguiente)
                recorrer(siguiente,destino,recorrido)

        recorrido = [destino]
        recorrer(destino,origen,recorrido)
        return recorrido[::-1]
    
    def camino_bellman_ford(self,origen,destino)->list[T]:
        """Este si permite pesos negativos"""
        def init():
            pasadas = dict()
            for nodo in self.vertices:
                if nodo == origen:
                    pasadas[nodo]={"antecesor":None,"costo":0} #seria infinito pero no quiero importar math
                else:
                    pasadas[nodo]={"antecesor":None,"costo":99999999} #seria infinito pero no quiero importar math
            return pasadas
        dict_pasadas = init()


        def marcar(origen,sin_visitar:list[T],hayCambio = False):
            if sin_visitar:
                nodo_minimo = origen
                vecinos = self.vecinos_de(nodo_minimo)
                for vecino in vecinos:
                    if vecino in sin_visitar:        
                        if dict_pasadas[vecino]["costo"] > dict_pasadas[nodo_minimo]["costo"] + self.aristas[nodo_minimo][vecino]:
                            dict_pasadas[vecino]["antecesor"]=nodo_minimo
                            dict_pasadas[vecino]["costo"] = dict_pasadas[nodo_minimo]["costo"] + self.aristas[nodo_minimo][vecino]
                            hayCambio=True
                vecino_minimo:T|None = None
                costo_minimo = 99999999999
                for vecino in vecinos:
                    if vecino in sin_visitar:
                        if costo_minimo>dict_pasadas[vecino]["costo"]:
                            vecino_minimo = vecino
                            costo_minimo = dict_pasadas[vecino]["costo"]
                if vecino_minimo is not None:
                    sin_visitar.remove(vecino_minimo)
                    marcar(vecino_minimo,sin_visitar)
            

        sin_visitar = list(self.vertices)
        sin_visitar.remove(origen)
        marcar(origen,sin_visitar)





        
        
        
        
        
        
        return []
    

if __name__ == "__main__":
    # t = GrafoAdyacencia()
    # t.agregar_nodo("a")
    # t.agregar_nodo("b")
    # t.agregar_nodo("c")
    # t.agregar_nodo("d")
    # t.agregar_nodo("e")
    # t.agregar_nodo("f")

    # t.agregar_arista(("a","b"),5)
    # t.agregar_arista(("a","c"),2)
    # t.agregar_arista(("a","d"),3)
    # t.agregar_arista(("c","b"),1)
    # t.agregar_arista(("d","e"),2)
    # t.agregar_arista(("e","f"),1)
    # t.agregar_arista(("b","f"),3)
    # t.agregar_arista(("b","e"),1)

    # print(t.camino_minimo("a","f"))

    a = set([1,2])
    b = set([2,1])
    print(a==b)






