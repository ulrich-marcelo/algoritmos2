from typing import Union, TypeAlias

__all__=["Nat","Cero","Suc","cero","suc","es_cero"]

Nat: TypeAlias = Union["Cero", "Suc"]

class Cero:
    def __repr__(self):
        return 'Cero'
    
    def __eq__(self, otro : "Nat") -> bool:
        return isinstance(otro,Cero)
    def __hash__(self) -> int:
        return 0
    def __lt__(self,otro: Nat) -> bool:
        return False

class Suc:
    def __init__(self, pred: Nat):
        self.pred = pred

    def __repr__(self):
        return f'Suc({self.pred.__repr__()})'
    
    def __eq__(self, otro :Nat) -> bool:
        return isinstance(otro,Suc) and igual(self,otro)
    
    def __hash__(self) -> int:

        return hash(self.__repr__())
    def __lt__(self,otro:Nat):
        return isinstance(otro,Suc) and menor(self,otro) 
    def __sub__(self,otro:Nat):
        if isinstance(otro,Suc):
            return resta(self,otro)
        elif isinstance(otro,Cero):
            return self
        else:
            raise TypeError("O con Suc o Cero, enfermo")  
  
    

def cero() -> Nat:
    return Cero()

def suc(n: Nat) -> Nat:
    return Suc(n)

def es_cero(n: Nat) -> bool:
    return isinstance(n, Cero)


def pred(n: Nat) -> Nat:
    if es_cero(n):
        raise ValueError('cero no tiene predecesor')
    else:
        return n.pred

def nat_to_int(n: Nat) -> int:
    if es_cero(n):
        return 0
    else:
        return 1 + nat_to_int(pred(n))
    
def suma(x: Nat, y: Nat) -> Nat:
    if es_cero(x):
        return y
    else:
        return suma(pred(x), suc(y))
    
def igual(x:Nat,y:Nat)->bool:
    if es_cero(x) and es_cero(y):
        return True
    elif es_cero(x) or es_cero(y):
        return False
    else:
        return igual(x.pred,y.pred)

def menor(x:Nat,y:Nat)->bool:
    if es_cero(y):
        return not es_cero(x)
    elif es_cero(x): 
        return True
    else:
        return menor(x.pred,y.pred)
    

def resta(x:Nat,y:Nat)->Nat:
    if not es_cero(x) and not es_cero(y):
        x= pred(x)
        y=pred(y)
        return resta(x,y)
    else:
        return x


nulo = cero()
uno = Suc(nulo)
dos=Suc(uno)

print(dos == dos)

print(dos == uno)

print(uno == dos)