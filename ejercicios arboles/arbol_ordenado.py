from typing import TypeVar, Optional, Protocol
from arbol_con_mariano import ArbolBinario, NodoAB

class Comparable(Protocol):
    def __lt__(self: 'T', otro: 'T') -> bool: ...
    def __le__(self: 'T', otro: 'T') -> bool: ...
    def __gt__(self: 'T', otro: 'T') -> bool: ...
    def __ge__(self: 'T', otro: 'T') -> bool: ...
    def __eq__(self: 'T', otro: 'T') -> bool: ...
    def __ne__(self: 'T', otro: 'T') -> bool: ...

T = TypeVar('T', bound=Comparable)


class NodoABO(NodoAB[T]):
    def __init__(self, dato: T):
        super().__init__(dato, ArbolBinarioOrdenado(), ArbolBinarioOrdenado())
    
    def __lt__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato < otro.dato
    
    def __gt__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato > otro.dato

    def __eq__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato == otro.dato
    
    
class ArbolBinarioOrdenado(ArbolBinario[T]):
    @staticmethod
    def crear_nodo(dato: T) -> "ArbolBinarioOrdenado[T]":
        nuevo = ArbolBinarioOrdenado()
        nuevo.set_raiz(NodoABO(dato))
        return nuevo
    
    def es_ordenado(self) -> bool:
        def es_ordenado_interna(
            arbol: "ArbolBinarioOrdenado[T]", 
            minimo: Optional[T] = None, 
            maximo: Optional[T] = None
        ) -> bool:
            if arbol.es_vacio():
                return True
            if (minimo is not None and arbol.dato() <= minimo) or (maximo is not None and arbol.dato() >= maximo):
                return False
            return es_ordenado_interna(arbol.si(), minimo, arbol.dato()) and es_ordenado_interna(arbol.sd(), arbol.dato(), maximo)
        
        return es_ordenado_interna(self)
    
    def insertar_si(self, arbol: "ArbolBinarioOrdenado[T]"):
        si = self.si()
        super().insertar_si(arbol)
        if not self.es_ordenado():
            super().insertar_si(si)
            raise ValueError("El árbol a insertar no es ordenado o viola la propiedad de orden del árbol actual")
    
    def insertar_sd(self, arbol: "ArbolBinarioOrdenado[T]"):
        sd = self.sd()
        super().insertar_sd(arbol)
        if not self.es_ordenado():
            super().insertar_sd(sd)
            raise ValueError("El árbol a insertar no es ordenado o viola la propiedad de orden del árbol actual")
    
    def insertar(self, valor: T):
        if self.es_vacio():
            self.set_raiz(NodoABO(valor))
        elif valor == self.dato():
            raise ValueError("No se admiten repetidos!")
        elif valor < self.dato():
            self.si().insertar(valor)
        else:
            self.sd().insertar(valor)

    

    @staticmethod
    def convertir_ordenado(arbol_binario: ArbolBinario[T]) -> "ArbolBinarioOrdenado[T]":
        pass





    def pertenece(self,valor : T) -> bool:
        def buscar_interna(
            arbol: "ArbolBinarioOrdenado[T]", 
        ) -> bool:
            if arbol.es_vacio():
                return False
            elif valor == arbol.dato():
                return True
            return buscar_interna(arbol.si()) or buscar_interna(arbol.sd())
        
        return buscar_interna(self)
    

    def max(self) -> "ArbolBinarioOrdenado[T]":
        if self.es_vacio():
            raise ValueError("AV no tiene max")
        elif not self.sd().es_vacio():
            return self.sd().max()
        else:
            return self
    def max_con_pred(self)-> tuple["ArbolBinarioOrdenado[T]|None","ArbolBinarioOrdenado[T]|None"]: 
        if self.es_vacio():
            return None,None
        elif self.sd().es_vacio():
            return self,None
        elif self.sd().sd().es_vacio():
            return self.sd(),self
        else:
            return self.sd().max_con_pred()

    def eliminar(self,valor:T) -> None:
        def eliminar_fusion(t: ArbolBinarioOrdenado[T])->None:
            t.si().max().insertar_sd(t.sd())
            t.raiz = t.si().raiz

        def eliminar_copia(t: ArbolBinarioOrdenado[T]):
            max,pred = t.si().max_con_pred()
            if max is not None and pred is not None:
                t.raiz.dato = max.dato()
                pred.insertar_sd(max.si())



        if self.es_vacio():
            return
        elif self.dato() == valor:
            if self.es_hoja():
                self.raiz = None
            elif not self.sd().es_vacio() and not self.si().es_vacio():
                eliminar_fusion(self)
            elif not self.sd().es_vacio():
                self.raiz = self.sd().raiz
            else:
                self.raiz = self.si().raiz
        elif valor < self.dato():
            self.si().eliminar(valor)
        else:
            self.sd().eliminar(valor)


        


        

    
    


        

def main():
    t: ArbolBinarioOrdenado[int] = ArbolBinarioOrdenado()
    t.insertar(10)
    t.insertar(5)
    t.insertar(15)
    t.insertar(2)
    t.insertar(7)
    t.insertar(12)
    t.insertar(17)
    t.insertar(20)
    t.insertar(13)
    print(t.es_ordenado())
    print(t)

    t2: ArbolBinarioOrdenado[int] = ArbolBinarioOrdenado()
    t2.insertar(8)
    # t2.insertar(11)   # Descomentar para probar la excepción al violar el orden
    t2.insertar(6)
    t.insertar_si(t2)
    print(t)
    print(f'Ordenado?: {t.es_ordenado()}')

    print(f'Tiene 12: {t.pertenece(12)}')

    t.eliminar(15)
    print(t)

if __name__ == "__main__":
    main()