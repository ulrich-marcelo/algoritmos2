#Arbol binario generico clasico, usando el arbol vacio

from typing import Generic, Optional, TypeVar, Callable, Any
from functools import wraps

T = TypeVar("T")

class NodoAB(Generic[T]):
    def __init__(self,dato:T) -> None:
        self.valor = dato
        self.si : ArbolBinario[T] = ArbolBinario()
        self.sd : ArbolBinario[T] = ArbolBinario()


class ArbolBinario(Generic[T]):

    class Decoradores:
        @classmethod
        def validar_no_es_vacio(cls,f:Callable[...,Any])-> Callable[...,Any]:
            @wraps(f)
            def wrapper(self,*args,**kwargs) -> Any:
                if self.es_vacio():
                    raise TypeError("Arbol Vacio")
                return f(self,*args,*kwargs)
            return wrapper


    def __init__(self) -> None:
        self.raiz = None


    @staticmethod #Se usa para tener una funcion que podria estar afuera, adentro. Asi empaquetamos. NO LE PASAMOS SELF, eso es para metodos de instancia
    def crear_nodo(dato:T) -> "ArbolBinario[T]":
        nuevo = ArbolBinario()
        nuevo.raiz = NodoAB(dato)
        return nuevo
    
    def es_vacio(self)->bool:
        return self.raiz is None
    
    
    
    @Decoradores.validar_no_es_vacio
    def si(self) -> "ArbolBinario[T]":
        
        return self.raiz.si #type:ignore

    @Decoradores.validar_no_es_vacio
    def sd(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            raise TypeError("Arbol Vacio")
        return self.raiz.sd #type:ignore

    @Decoradores.validar_no_es_vacio
    def dato(self)-> T:
        return self.raiz.valor #type:ignore

    @Decoradores.validar_no_es_vacio
    def insertar_si(self,si:"ArbolBinario[T]"):
        self.raiz.si = si #type:ignore

    @Decoradores.validar_no_es_vacio
    def insertar_sd(self,sd:"ArbolBinario[T]"):
        self.raiz.sd = sd #type:ignore

    def insertar_raiz(self,dato : T):
        self.raiz = NodoAB(dato)

    
    def altura(self)->int:
        if self.es_vacio():
            return 0
        else:
            return 1 + max(self.si().altura(),self.sd().altura())
        
    def __len__(self)->int:
        if self.es_vacio():
            return 0
        else:
            return 1 + len(self.si()) + len(self.sd())



    def preorden(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return  [self.dato()] + self.si().preorden() + self.sd().preorden() 

    def inorden(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return   self.si().preorden()+ [self.dato()] + self.sd().preorden() 

    def postorden(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return   self.si().preorden() + self.sd().preorden() + [self.dato()]  
    
    def __str__(self):
        def recorrer(t: ArbolBinario[T],nivel:int) -> str:
            tab = "_"*4*nivel
            if t.es_vacio():
                return tab + "AV\n"
            else:

                tab += str(t.dato()) + "\n"
                tab += recorrer(t.si(),nivel+1)
                tab += recorrer(t.sd(),nivel+1)
                return tab
        return recorrer(self,0)
    

    def copy(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario()
        else:
            copia = ArbolBinario.crear_nodo(self.dato())
            copia.insertar_si(self.si().copy())
            copia.insertar_sd(self.sd().copy())
            return copia
    

    def bfs(self)->list[T]:
        
        def _bfs(cola: list[ArbolBinario[T]],camino:list[T]) -> list[T]:

            if not cola:
                return camino
            else:
                actual = cola.pop(0)
                if not actual.es_vacio():    
                    camino.append(actual.dato())
                    cola.append(actual.si())
                    cola.append(actual.sd())
                return _bfs(cola,camino)

        return _bfs([self],[])
        
        

if __name__ == "__main__":
    t = ArbolBinario.crear_nodo(1)
    n2 = ArbolBinario.crear_nodo(2)
    n3 = ArbolBinario.crear_nodo(3)
    n4 = ArbolBinario.crear_nodo(4)
    n5 = ArbolBinario.crear_nodo(5)
    n6 = ArbolBinario.crear_nodo(6)
    n7 = ArbolBinario.crear_nodo(7)
    n8 = ArbolBinario.crear_nodo(8)
    n9 = ArbolBinario.crear_nodo(9)

    t.insertar_si(n2)
    t.insertar_sd(n3)

    n2.insertar_si(n4)
    n2. insertar_sd(n5)

    n4.insertar_si(n8)
    n4.insertar_sd(n9)

    n3.insertar_si(n6)
    n3.insertar_sd(n7)

    print(t.bfs())











