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
    

class grafoMatrizAdyacencia():
    def __init__(self) -> None:
        self.indices = []
        self.matriz = []

    def agregar_nodo(self,nodo : int) -> None:
        self.indices.append(nodo)
        for fila in self.matriz:
            fila.append(0)
        self.matriz.append([ 0 for nodo in self.indices])

    def agregar_arista(self,nodoA : int,nodoB : int) -> None:
        indiceA = self.indices.index(nodoA)
        indiceB = self.indices.index(nodoB)
        self.matriz[indiceA][indiceB] = 1
        self.matriz[indiceB][indiceA] = 1

    def eliminar_nodo(self,nodo)->None:
        indice = self.indices.index(nodo)
        self.matriz.pop(indice)
        for fila in self.matriz:
            fila.pop(indice)
        self.indices.pop(indice)

    def eliminar_arista(self,nodoA,nodoB) -> None:
        indiceA = self.indices.index(nodoA)
        indiceB = self.indices.index(nodoB)
        self.matriz[indiceA][indiceB]=0
        self.matriz[indiceB][indiceA]=0

    def es_vecino_de(self,nodoA,nodoB)->bool:
        indiceA = self.indices.index(nodoA)
        indiceB = self.indices.index(nodoB)
        return self.matriz[indiceA][indiceB]!=0
    
    def vecinos_de(self,nodo) -> list[int]:
        indice = self.indices.index(nodo)
        vecinos = self.matriz[indice]
        return [self.indices[i] for i in range(len(vecinos)) if vecinos[i]!=0]

    def __str__(self):
        string = f"Nodos: {self.indices}\n"
        for fila in self.matriz:
            string += str(fila) + "\n"
        return string





    
graf = grafoMatrizAdyacencia()
graf.agregar_nodo(1)
graf.agregar_nodo(2)
graf.agregar_nodo(3)
graf.agregar_nodo(4)

graf.agregar_arista(1,2)
graf.agregar_arista(1,3)
graf.agregar_arista(2,4)
graf.agregar_arista(3,4)
print(graf)

graf.eliminar_arista(1,2)
print(graf)

graf.eliminar_nodo(2)
print(graf)

print(graf.vecinos_de(3))
print(graf.es_vecino_de(1,4))







