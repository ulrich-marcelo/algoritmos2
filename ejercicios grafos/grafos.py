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
from typing import Generic, TypeVar, Optional
T = TypeVar('T')

class Grafo(Generic[T]):
    def __init__(self, vertices: list[T]=[],aristas: list[tuple[T]]=[]) -> None:
        self.vertices = vertices
        self.aristas = aristas
    
    def agregar_nodo(self,nodo:T) -> None:
        if not nodo in self.vertices:
            self.vertices.append(nodo)
        else:
            raise ValueError(f"El nodo {nodo} ya pertenece al grafo.")

    def agregar_arista(self,arista:tuple[T]) -> None:
        opuesta = arista[::-1]
        if arista in self.aristas:
            raise ValueError(f"La arista {arista} ya pertenece al grafo")
        elif opuesta in self.aristas:
            raise ValueError(f"La arista {opuesta} ya pertenece al grafo")
        else:
            self.aristas.append(arista)

    def eliminar_nodo(self,nodo:T) -> None:
        if not nodo in self.vertices:
            raise ValueError(f"El nodo {nodo} no pertenece al grafo.")
        else:
            self.vertices.remove(nodo)

    def eliminar_arista(self,arista:tuple[T]) -> None:
        if arista not in self.aristas:
            raise ValueError(f"El nodo {arista} no pertenece al grafo.")
        else:
            self.aristas.remove(arista)

    def es_vecino_de(self,nodoA:T,nodoB:T) -> bool:
        ab = (nodoA,nodoB)
        ba = (nodoB,nodoA)
        if ab in self.aristas or ba in self.aristas:
            return True
        else:
            return False
    
    def vecinos_de(self,nodo:T) -> list[T]:
        vecinos = []
        for arista in self.aristas:
            if nodo in arista:
                vecinos.append(arista[not arista.index(nodo)])
        return vecinos



class GrafoV2(Generic[T]):
    def __init__(self, vertices: set[T]={},aristas: list[tuple[T]]=[]) -> None:
        self.vertices = vertices
        self.aristas = aristas

    def agregar_nodo(self,nodo:T) -> None:
        if not nodo in self.vertices:
            self.vertices.append(nodo)
        else:
            raise ValueError(f"El nodo {nodo} ya pertenece al grafo.")

    def agregar_arista(self,arista:tuple[T]) -> None:
        opuesta = arista[::-1]
        if arista in self.aristas:
            raise ValueError(f"La arista {arista} ya pertenece al grafo")
        elif opuesta in self.aristas:
            raise ValueError(f"La arista {opuesta} ya pertenece al grafo")
        else:
            self.aristas.append(arista)

    def eliminar_nodo(self,nodo:T) -> None:
        if not nodo in self.vertices:
            raise ValueError(f"El nodo {nodo} no pertenece al grafo.")
        else:
            self.vertices.remove(nodo)

    def eliminar_arista(self,arista:tuple[T]) -> None:
        if arista not in self.aristas:
            raise ValueError(f"El nodo {arista} no pertenece al grafo.")
        else:
            self.aristas.remove(arista)

    def es_vecino_de(self,nodoA:T,nodoB:T) -> bool:
        ab = (nodoA,nodoB)
        ba = (nodoB,nodoA)
        if ab in self.aristas or ba in self.aristas:
            return True
        else:
            return False
    
    def vecinos_de(self,nodo:T) -> list[T]:
        vecinos = []
        for arista in self.aristas:
            if nodo in arista:
                vecinos.append(arista[not arista.index(nodo)])
        return vecinos




class GrafoAdyacencia(Generic[T]):
    def __init__(self, vertices: set[T]=set(),aristas: dict[T : set[T] ]= {}) -> None:
        self.vertices = vertices
        self.aristas = aristas

    def agregar_nodo(self,nodo:T) -> None:
        self.vertices.add(nodo)
        self.aristas[nodo] = set()

    def agregar_arista(self,arista:tuple[T]) -> None:
        self.aristas[arista[0]].add(arista[1])
        self.aristas[arista[1]].add(arista[0])

    def eliminar_nodo(self,nodo:T) -> None:
        self.vertices.discard(nodo)

    def eliminar_arista(self,arista:tuple[T]) -> None:
        self.aristas[arista[0]].discard(arista[1])
        self.aristas[arista[1]].discard(arista[0])

    def es_vecino_de(self,nodoA:T,nodoB:T) -> bool:
        return nodoB in self.aristas[nodoA]
    
    def vecinos_de(self,nodo:T) -> list[T]:
        return self.aristas[nodo]
    
    def __str__(self) -> str:
        return f"Vertices = {self.vertices} \n Aristas = {self.aristas}"
    

graf = GrafoAdyacencia()

graf.agregar_nodo(1)
graf.agregar_nodo(2)
print(graf)
graf.agregar_arista((1,2))
print(graf)













