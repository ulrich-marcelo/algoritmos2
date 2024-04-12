#Tengo una mochila con limite de peso. Tengo varias cosas.
#Cada cosa tiene peso y valor.
#Como maximizar el valor teniendo en cuenta el limite de peso?

'''
Podriamos hacer todas las combinaciones y evaluar valores: problema, costoso
Y si hago algorimo greedy?
    Ordeno por peso y busco combinaciones locales.
        problema: maximo local
    Si se puede fraccional? ordeno por valor/peso?
'''
from dataclasses import dataclass
from functools import reduce

@dataclass
class ItemMochila():
    peso: float
    valor:float
    def valorAjustado(self) ->float:
        return self.valor/self.peso
    def __gt__(self,other)->bool:
        return self.peso > other.peso



class Mochila():
    def __init__(self,capacidad:float) -> None:
        self.capacidad = capacidad
        self.contenido = []

    def valor(self) -> float:
        return reduce(lambda acc,y: acc + y.valorAjustado(),self.contenido,0)
    
    def entraItem(self,item:ItemMochila)->bool:
        return self.pesoDisponible()>item.peso
    
    def pesoDisponible(self)->float:
        return self.capacidad - reduce(lambda acc,actual:acc + actual.peso,self.contenido,0)
    
    def agregar(self,item:ItemMochila):
        if self.entraItem(item):
            self.contenido.append(item)
        else:
            raise ValueError("NO ENTRA")
    
    def agregarFraccion(self,item):
        nuevo_peso = min(self.pesoDisponible(),item.peso)
        nuevo_valor = item.valor 


    def __str__(self) -> str:
        ret = f'Peso Disponible: {self.pesoDisponible()}\n'
        ret+= f'Valor: {self.valor()}\n'
        ret+= str(self.contenido)
        return ret
    
    def optimizarGreedy(self,items: list[ItemMochila]):
        def optimizar(items):
            item = items[0]
            if self.entraItem(item):
                self.agregar(item)
                optimizar(items[1:])
        items.sort(reverse=True) #type: ignore
        optimizar(items)
        

if __name__ == "__main__":
    items = [
        ItemMochila(2.4,10),
        ItemMochila(3.5,20),
        ItemMochila(4.6,5),
        ItemMochila(8.9,6),
        ItemMochila(20,50)   
    ]

    mochi = Mochila(40)
    print(mochi)
    mochi.optimizarGreedy(items)
    print(mochi)











