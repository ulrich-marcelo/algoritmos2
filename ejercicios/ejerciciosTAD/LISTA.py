from typing import Generic, TypeVar, Optional, TypeAlias
from copy import copy

T = TypeVar('T')
ListaGenerica: TypeAlias = "Lista[T]"

class Nodo(Generic[T]):
    def __init__(self, dato: T, sig: Optional[ListaGenerica] = None):
        self.dato = dato
        if sig is None:
            self.sig= Lista()
        else:
            self.sig = sig

    

class Lista(Generic[T]):
    def __init__(self):
        self._head: Optional[Nodo[T]] = None
    
    def insertar(self, dato: T):
        actual = copy(self)
        self._head = Nodo(dato, actual)

    def es_vacia(self) -> bool:
        return self._head is None

    def head(self) -> T:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.dato
        
    def tail(self) -> ListaGenerica:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return copy(self._head.sig)
        
    def copy(self) -> ListaGenerica:
        if self.es_vacia():
            return Lista()
        else:
            parcial = self._head.sig.copy()
            actual = Lista()
            actual._head = Nodo(copy(self._head.dato), parcial)
            return actual
        
    def tail(self) -> ListaGenerica:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.sig.copy()
        
    def __len__(self) -> int:
        if self.es_vacia():
            return 0
        else:
            return 1 + self.tail().__len__()

        
    def __repr__(self) -> str:
        def interna(lista:ListaGenerica):
            if lista.es_vacia():
                return ""
            else:
                return f"{lista.head()} {lista.tail().__repr__()}"
        return f"[{interna(self)}]"
    
    def __str__(self) -> str:
        def interna(lista:ListaGenerica):
            if self.es_vacia():
                return ""
            else:
                return f"{self.head()} {self.tail().__repr__()}"
        return f"[{interna(self)}]"


    def reversa(self) -> ListaGenerica:
        copia = self.copy()
        nueva = Lista()
        while not copia.es_vacia():
            nueva.insertar(copia.head())
            copia = copia.tail()
        return nueva


    def reversa_cola(self)-> ListaGenerica:
        def interna(original : ListaGenerica, reversa : ListaGenerica)->ListaGenerica:
            if not original.es_vacia():
                elemento = original.head()
                reversa.insertar(elemento)
                interna(original.tail(),reversa)
        nueva = Lista()
        interna(self,nueva)
        return nueva
    

xs = Lista()
for i in range(3):
    xs.insertar(Nodo(i,xs))
xs_reversa = xs.reversa_cola()
print(xs_reversa.__repr__())




