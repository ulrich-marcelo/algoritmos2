from typing import Generic, Optional, TypeVar

T = TypeVar("T")

class Nodo(Generic[T]):
    def __init__(self,valor: T) -> None:
        self.valor = valor
        self.izquierda : Optional[Nodo] = None
        self.derecha : Optional[Nodo] = None
    def __str__(self):
        return str(self.valor)
    def __repr__(self) -> str:
        return str(self.valor)

class ArbolBinario(Generic[T]):
    def __init__(self, raiz : Optional[Nodo[T]] = None) -> None:
        self.raiz : Optional[Nodo[T]] = raiz

    def __str__(self) -> str:
        def preorden(nodo:Optional[Nodo[T]],orden:str = "")->str:
            if nodo:
                orden += str(nodo)
                orden += preorden(nodo.izquierda)
                orden += preorden(nodo.derecha)
                return orden
            else:
                return ""
        return preorden(self.raiz)
    
    def preorden(self)->str:
        def _preorden(nodo:Optional[Nodo[T]],orden:str = "")->str:
            if nodo:
                orden += str(nodo)
                orden += _preorden(nodo.izquierda)
                orden += _preorden(nodo.derecha)
                return orden
            else:
                return ""
        return _preorden(self.raiz)
    
    def postorden(self)->str:
        def _postorden(nodo:Optional[Nodo[T]],orden:str = "")->str:
            if nodo:
                orden += _postorden(nodo.izquierda)
                orden += _postorden(nodo.derecha)
                orden += str(nodo)
                return orden
            else:
                return ""
        return _postorden(self.raiz)
    
    def inorden(self)->str:
        def _inorden(nodo:Optional[Nodo[T]],orden:str = "")->str:
            if nodo:
                orden += _inorden(nodo.izquierda)
                orden += str(nodo)
                orden += _inorden(nodo.derecha)
                
                return orden
            else:
                return ""
        return _inorden(self.raiz)
    
    def es_vacio(self)->bool:
        return self.raiz is None
    
    def insertar(self,valor:T) ->None:
        def _insertar_recursivo(nodo:Optional[Nodo[T]],valor: T)->Nodo:
            if nodo is None:
                return Nodo(valor)
            elif nodo.izquierda is None:
                nodo.izquierda = _insertar_recursivo(nodo.izquierda,valor)
            else:
                nodo.derecha = _insertar_recursivo(nodo.derecha,valor)
            return nodo
        if self.es_vacio():
            self.raiz = Nodo(valor)
        else:
            self.raiz = _insertar_recursivo(self.raiz,valor)

    def eliminar(self,valor:T) ->None:
        def _eliminar_recursivo(nodo:Optional[Nodo[T]],valor:T) ->Optional[Nodo[T]]:
            if nodo and nodo.valor != valor:
                nodo.izquierda = _eliminar_recursivo(nodo.izquierda,valor)
                nodo.derecha = _eliminar_recursivo(nodo.derecha,valor)
            return nodo
        if not self.es_vacio():
            self.raiz = _eliminar_recursivo(self.raiz,valor)

    def cantidad_nodos(self, contador :Optional[int] = 0):
        def _cantidad_nodos_interno(nodo:Optional[Nodo],contador : int=0)->int:
            if nodo:
                contador +=1
                contador += _cantidad_nodos_interno(nodo.izquierda)
                contador +=_cantidad_nodos_interno(nodo.derecha)
                return contador
            else:
                return 0
        
        if not self.es_vacio():
            return _cantidad_nodos_interno(self.raiz)
        else:
            return 0
        
    def altura(self):
        def _altura(nodo : Optional[Nodo[T]])->int:
            if nodo:
                altura_izq = _altura(nodo.izquierda)
                altura_der = _altura(nodo.derecha)
                return max([altura_izq,altura_der])+1
            else:
                return 0
        return _altura(self.raiz) if not self.es_vacio() else 0
    
    def nivel(self,valor:T)->int:
        def _nivel(nodo: Optional[Nodo[T]],valorBuscado:T,nivel :int = 1)->int:
            if nodo is None:
                return self.altura() +1
            elif nodo.valor == valor:
                return nivel
            else:
                nivel_izq = _nivel(nodo.izquierda,valor,nivel + 1)
                nivel_der = _nivel(nodo.derecha,valor,nivel + 1)
                return min(nivel_izq,nivel_der)
        return _nivel(self.raiz,valor)
    
    def subarbol(self,nodoBuscado: Nodo[T],izquierdo = True)-> "ArbolBinario[Nodo[T]]":
        def _subarbol(nodo:Optional[Nodo[T]],izquierdo:bool):
            if nodo: 
                if nodo.valor == nodoBuscado.valor:
                    if izquierdo:
                        return ArbolBinario(nodo.izquierda)
                    else:
                        return ArbolBinario(nodo.derecha)
                else: 
                    arbolIzq=_subarbol(nodo.izquierda,izquierdo)
                    arbolDer=_subarbol(nodo.derecha,izquierdo)
                    if not arbolIzq.raiz is None:
                        return arbolIzq
                    elif not arbolDer.raiz is None:
                        return arbolDer
                    else:
                        return ArbolBinario()
                    
            else:
                return ArbolBinario()
        return _subarbol(self.raiz,izquierdo)




     


arbol = ArbolBinario(Nodo(1))
for i in range(2,7):
    arbol.insertar(i)
print(str(arbol))
print(arbol.preorden())
print(arbol.postorden())
print(arbol.inorden())