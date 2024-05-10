from typing import Generic, TypeVar, Optional
from functools import reduce

T = TypeVar('T')

class ArbolN(Generic[T]):
    def __init__(self, dato: T):
        self._dato: T = dato
        self._subarboles: list[ArbolN[T]] = []
       
    @property
    def dato(self) -> T:
        return self._dato

    @dato.setter
    def dato(self, valor: T):
        self._dato = valor

    @property
    def subarboles(self) -> "list[ArbolN[T]]":
        return self._subarboles
    
    @subarboles.setter
    def subarboles(self, subarboles: "list[ArbolN[T]]"):
        self._subarboles = subarboles

    def insertar_subarbol(self, subarbol: "ArbolN[T]"):
        self.subarboles.append(subarbol)

    def es_hoja(self) -> bool:
        return self.subarboles == []
    
    def altura(self) -> int:
        def altura_n(bosque: list[ArbolN[T]]) -> int:
            if not bosque:
                return 0
            else:
                return max(bosque[0].altura(), altura_n(bosque[1:]))
        
        return 1 + altura_n(self.subarboles)
        
    def __len__(self) -> int:
        if self.es_hoja():
            return 1
        else:
            return 1 + sum([len(subarbol) for subarbol in self.subarboles])

    def __str__(self):
        def mostrar(t: ArbolN[T], nivel: int):
            tab = '.' * 4
            indent = tab * nivel
            out = indent + str(t.dato) + '\n'
            for subarbol in t.subarboles:
                out += mostrar(subarbol, nivel + 1)
            return out
            
        return mostrar(self, 0)

    def preorder(self) -> list[T]:
        return reduce(lambda recorrido, subarbol: recorrido + subarbol.preorder(), self.subarboles, [self.dato])

    def preorder2(self) -> list[T]:
        recorrido = [self.dato]
        for subarbol in self.subarboles:
            recorrido += subarbol.preorder2()
        return recorrido
    
    def preorder3(self) -> list[T]:
        def preorder_n(bosque: list[ArbolN[T]]) -> list[T]:
            return [] if not bosque else bosque[0].preorder3() + preorder_n(bosque[1:])
        return [self.dato] + preorder_n(self.subarboles)
    
    def __eq__(self, otro: "ArbolN[T]") -> bool: #type:ignore
        pass

    def bfs(self) -> list[T]: #type:ignore
        def recorrer():
            if q:
                actual = q.pop()
                lista.append(actual.dato)
                for subarbol in actual.subarboles:
                    q.insert(0,subarbol)#type:ignore
                recorrer()
        q = [self]
        lista = []
        recorrer()
        return lista
    
    def postorder(self) -> list[T]: #type:ignore
        return reduce(lambda recorrido, subarbol:   subarbol.postorder() + recorrido, self.subarboles[::-1], [self.dato])

    def postorder2(self) -> list[T]:
        recorrido = [self.dato]
        for subarbol in self.subarboles[::-1]:
            recorrido = subarbol.postorder2() + recorrido
        return recorrido
    
    def postorder3(self) -> list[T]:
        def postorder_n(bosque: list[ArbolN[T]]) -> list[T]:
            return [] if not bosque else postorder_n(bosque[1:]) + bosque[0].postorder3()
        return postorder_n(self.subarboles[::-1]) + [self.dato]


    def nivel(self,x:T) -> int:
        def nivel_n(lista,acum) -> int:
            if not lista:
                return 0
            else:
                index = max([n.nivel(x) for n in lista])
                return index + acum if index>0 else 0
        if self.es_hoja():
            return 0
        elif self.dato == x:
            return 1
        else:
            return nivel_n(self.subarboles,0) 



    def nivel2(self, x: T) -> int: #type:ignore
        if self.es_hoja():
            return  0
        elif self.dato == x:
            return 1
        else:
            lista_busqueda = [n.nivel(x) for n in self.subarboles]
            return max(lista_busqueda) + 1 if sum(lista_busqueda)>0 else 0
        
    def nivel3(self,x:T): #de tomi
        def buscar(t,x):
            if x== t.dato:
                return 1,True
            elif t.es_hoja():
                return 2,False
            else:
                found = False
                n=0
                i=0
                while not found and i< len(t.subarboles):
                    m,found = buscar(t.subarboles[i],x)
                    if not found:
                        n = max(n,m)
                    i +=1
                return n+1,found
        return buscar(self,x)[0]
        


    def ramas(self) -> list[list[T]]:
        if self.es_hoja():
            return [[self.dato]]
        else:
            ramas = []
            for subarbol in self.subarboles:
                ramas += subarbol.ramas()
            return [ [self.dato]+rama for rama in ramas]
        
    def ramas2(self) -> list[list[T]]:
        if self.es_hoja():
            return [[self.dato]]
        else:
            return [[self.dato]+rama[0] for rama in [[]+subarbol.ramas() for subarbol in self.subarboles]]
        
            

    #antecesores y sin ramas
    
    def antecesores(self,dato:T) ->list[T]:
        # caso base 1: self.dato == dato
        # caso base 2: self.es_hoja() y no es valor
        # caso recursivo: no es hoja y 
        if self.dato == dato:
            return [dato]
        elif self.es_hoja():
            return []
        else:
            i=0
            res = []
            while i< len(self.subarboles) and not res:
                res = self.subarboles[i].antecesores(dato)
                i+=1
            if res:
                if res[0] == dato:
                    res.pop()
                res.insert(0,self.dato)
            return res
    
    def antecesores2(self,dato:T) -> list[T]:
        def interna(arbol:ArbolN) ->list[T]:
            if arbol.dato == dato:
                return [dato]
            elif arbol.es_hoja():
                return []
            else:
                i=0
                res = []
                while i<len(arbol.subarboles) and not res:
                    res = interna(arbol.subarboles[i])
                    i+=1
                if res:
                    res.insert(0,arbol.dato)
                return res
        res = interna(self)
        res.pop()
        return res
    
    
    def antecesores3(self,dato:T) ->list[T]:
        # caso base 1: self.dato == dato
        # caso base 2: self.es_hoja() y no es valor
        # caso recursivo: no es hoja y 
        if self.dato == dato or self.es_hoja():
            return []
        else:
            i=0
            res = []
            encontrado = False
            while i< len(self.subarboles) and not encontrado:
                if self.subarboles[i]==dato:
                    encontrado = True
                else: 
                    res = self.subarboles[i].antecesores(dato)
                    encontrado = bool(res)
                i+=1
            if encontrado:
                res.insert(0,self.dato)
            return res
        
    def antecesores4(self,dato:T)->list[T]:
        def interna(arbol:ArbolN,antecesores : list[T])->list[T]:
            if arbol.dato == dato:
                return antecesores
            elif arbol.es_hoja():
                return []
            else:
                antecesores.append(arbol.dato)
                i=0
                res = []
                while i<len(arbol.subarboles) and not res:
                    res = interna(arbol.subarboles[i],antecesores.copy())
                    i+=1
                return res        
        return interna(self,[])


    def copy(self) -> "ArbolN[T]": #type:ignore
        pass
        
    def sin_hojas(self) -> "ArbolN[T]": #type:ignore
        for sub in self.subarboles:
            if not sub.es_hoja():
                self.insertar_subarbol(sub.sin_hojas())
            self.subarboles.remove(sub)
        return self

    
    def recorrido_guiado(self, direcciones: list[int]) -> Optional[T]:#type:ignore
        if not direcciones:
            return self.dato
        else:
                direc = direcciones.pop(0)
                if direc >= len(self.subarboles):
                    raise ValueError("No existe la direccion")
                return self.subarboles[direc].recorrido_guiado(direcciones)
     


def main():
    t = ArbolN(1)
    n2 = ArbolN(2)
    n3 = ArbolN(3)
    n4 = ArbolN(4)
    n5 = ArbolN(5)
    n6 = ArbolN(6)
    n7 = ArbolN(7)
    n8 = ArbolN(8)
    n9 = ArbolN(9)
    t.insertar_subarbol(n2)
    t.insertar_subarbol(n3)
    t.insertar_subarbol(n4)
    n2.insertar_subarbol(n5)
    n2.insertar_subarbol(n6)
    n4.insertar_subarbol(n7)
    n4.insertar_subarbol(n8)
    n7.insertar_subarbol(n9)
    
    print(t)
    print(t.antecesores4(9))
    print(t.recorrido_guiado([2,0,0]))
    


    print(f'Altura: {t.altura()}')
    print(f'Nodos: {len(t)}')

    print(f'BFS: {t.bfs()}')
    print(f'DFS preorder : {t.preorder()}')
    print(f'DFS preorder2: {t.preorder2()}')
    print(f'DFS preorder3: {t.preorder3()}')
    print(f'DFS postorder: {t.postorder()}')
    print(f'DFS postorder2: {t.postorder2()}')
    print(f'DFS postorder3: {t.postorder3()}')
    

    print(f'Nivel de 9: {t.nivel3(9)}')
    print(f'Nivel de 13: {t.nivel3(13)}')
    print(t.ramas2())
    print(t.sin_hojas())
    print(t)
    
    
    # t2 = t.copy()
    # t3 = t2.sin_hojas()
    # print(t)
    # print(t2)
    # print(t3)
    # print(f't == t2 {t == t2}')

    # print(f'recorrido_guiado [2,0,0]: {t2.recorrido_guiado([2,0,0])}')


if __name__ == '__main__':
    main()







