from typing import Generic, Optional, TypeVar, Callable,Any
from functools import wraps

T = TypeVar('T')



class ArbolBinario(Generic[T]):
    def __init__(self):
        self.raiz: Optional[NodoAB[T]] = None

    class _Decoradores:
        @classmethod
        def valida_es_vacio(cls, f: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(f)
            def wrapper(self, *args: Any, **kwargs: Any) -> Any:
                if self.es_vacio():
                    raise TypeError('Arbol Vacio')
                return f(self, *args, **kwargs)
            return wrapper
        
    @staticmethod
    def crear_nodo(dato: T, si: "Optional[ArbolBinario[T]]" = None, sd: "Optional[ArbolBinario[T]]" = None) -> "ArbolBinario[T]":
        t = ArbolBinario()
        t.raiz = NodoAB(dato, si, sd)
        return t

    def es_vacio(self) -> bool:
        return self.raiz is None

    def si(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        return self.raiz.si # type: ignore

    def sd(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        return self.raiz.sd # type: ignore

    def dato(self) -> T:
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        return self.raiz.dato # type: ignore

    def es_hoja(self) -> bool:
        return not self.es_vacio() and self.si().es_vacio() and self.sd().es_vacio()

    def insertar_si(self, si: "ArbolBinario[T]"):
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        self.raiz.si = si # type: ignore

    def insertar_sd(self, sd: "ArbolBinario[T]"):
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        self.raiz.sd = sd # type: ignore
    
    def altura(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + max(self.si().altura(), self.sd().altura())
        
    def __len__(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + len(self.si()) + len(self.sd())
        
    def nivel(self,dato:T) -> int:
        def _nivel(arbol:ArbolBinario,nivel = 1):
            if arbol.es_vacio():
                return self.altura() + 1
            elif arbol.dato() == dato:
                return nivel
            else:
                nivel_si = _nivel(arbol.si(),nivel + 1)
                nivel_sd = _nivel(arbol.sd(),nivel+1)
                nivel_buscado = min(nivel_sd,nivel_si)
                return nivel_buscado
        return _nivel(self)
    
    def __str__(self):
        def mostrar(t: ArbolBinario[T], nivel: int):
            tab = '.' * 4
            indent = tab * nivel
            if t.es_vacio():
                return indent + 'AV\n'
            else:
                out = indent + str(t.dato()) + '\n'
                out += mostrar(t.si(), nivel + 1)
                out += mostrar(t.sd(), nivel + 1)
                return out
            
        return mostrar(self, 0)
    
    def __eq__(self, otro: "ArbolBinario") -> bool:
        if self.es_hoja() or otro.es_hoja():
            if self.es_hoja() and otro.es_hoja():
                return self.dato() == otro.dato()
            else:
                return False
        else:
            if self.dato() == self.dato():
                if not self.sd().es_vacio() and not otro.sd().es_vacio():
                    return self.si() == otro.si() and self.sd() == otro.sd()
                else:
                    return self.si() == otro.si()
            else:
                return False
            
    def camino_guiado(self,camino:list[str]) -> T:
        if self.es_vacio():
            raise TypeError('Arbol Vacio')
        elif self.es_hoja():
            if len(camino) ==0:
                return self.dato()
            else:
                raise ValueError("Camino Invalido")
        else: 
            if not camino:
                return self.dato()
            else:
                instruccion = camino.pop(0)
                if instruccion == "izq":
                    return self.si().camino_guiado(camino)
                elif instruccion == "der":
                    if self.sd().es_vacio():
                        raise ValueError("Camino Invalido")
                    return self.sd().camino_guiado(camino)
                else:
                    raise ValueError("Las instrucciones deben ser o 'izq' o 'der'")
                
    def preorder(self)->str:
        def recorrer(arbol,recorrido:str = "") -> str:
            if not arbol.es_vacio():
                recorrido += str(arbol.dato())
                recorrido += recorrer(arbol.si(),"")
                recorrido += recorrer(arbol.sd(),"")
                return recorrido
            else:
                return  ""
        return recorrer(self,"")
    
    def inorder(self)->str:
        def recorrer(arbol,recorrido:str = "") -> str:
            if not arbol.es_vacio():
                recorrido += recorrer(arbol.si(),"")
                recorrido += str(arbol.dato())
                recorrido += recorrer(arbol.sd(),"")
                return recorrido
            else:
                return  ""
        return recorrer(self,"")
    def postorder(self)->str:
        def recorrer(arbol,recorrido:str = "") -> str:
            if not arbol.es_vacio():
                recorrido += recorrer(arbol.si(),"")
                recorrido += recorrer(arbol.sd(),"")
                recorrido += str(arbol.dato())
                return recorrido
            else:
                return  ""
        return recorrer(self,"")
    
    def bfs(self)->str:
        def recorrer(recorrido:str, cola:list[ArbolBinario]) ->str:
            if cola:
                arbol = cola.pop(0)
                recorrido+= str(arbol.dato())
                if arbol.es_hoja():
                    return recorrer(recorrido,cola)
                else:
                    cola.append(arbol.si())                    
                    if not arbol.sd().es_vacio():
                        cola.append(arbol.sd())
                    return recorrer(recorrido,cola)
            else:
                return recorrido
        return recorrer("",[self])
    

class NodoAB(Generic[T]):
    def __init__(
        self, 
        dato: T, 
        si: Optional[ArbolBinario[T]] = None,  
        sd: Optional[ArbolBinario[T]] = None 
    ):
        self.dato: T = dato
        self.si: ArbolBinario[T] = ArbolBinario() if si is None else si
        self.sd: ArbolBinario[T] = ArbolBinario() if sd is None else sd

if __name__ == "__main__":
    t = ArbolBinario.crear_nodo(1)
    n2 = ArbolBinario.crear_nodo(2)
    n3 = ArbolBinario.crear_nodo(3)
    n4 = ArbolBinario.crear_nodo(4)
    n5 = ArbolBinario.crear_nodo(5)
    n6 = ArbolBinario.crear_nodo(6)
    n7 = ArbolBinario.crear_nodo(7)
    n8 = ArbolBinario.crear_nodo(8)
    n2.insertar_si(n4)
    n2.insertar_sd(n5)
    n5.insertar_si(n8)
    n3.insertar_si(n6)
    n3.insertar_sd(n7)
    t.insertar_si(n2)
    t.insertar_sd(n3)

    t2 = ArbolBinario.crear_nodo(1)
    n22 = ArbolBinario.crear_nodo(2)
    n32 = ArbolBinario.crear_nodo(3)
    n42 = ArbolBinario.crear_nodo(4)
    n52 = ArbolBinario.crear_nodo(5)
    n62 = ArbolBinario.crear_nodo(6)
    n72 = ArbolBinario.crear_nodo(9)
    n82 = ArbolBinario.crear_nodo(9)
    n22.insertar_si(n42)
    n22.insertar_sd(n52)
    n52.insertar_si(n82)
    n32.insertar_si(n62)
    n32.insertar_sd(n72)
    t2.insertar_si(n22)
    t2.insertar_sd(n32)

    
    
    #print(t.camino_guiado(["izq","der","der"]))  
    print(t.preorder())
    print(t.inorder())
    print(t.postorder())
    print(t.bfs())
