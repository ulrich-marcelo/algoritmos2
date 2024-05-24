
class Vinculo:
    def __init__(self,label:str,destino:"Pagina") -> None:
        self.label = label
        self.destino = destino

    def get_destino(self)->"Pagina":
        return self.destino
    
    def __str__(self) -> str:
        return self.label


class Pagina:
    def __init__(self,nombre:str,contenido:str) ->None:
        self.nombre = nombre
        self.contenido = contenido
        self.vinculos : list[Vinculo] = []


    def agregar_vinculo(self,label:str,destino: "Pagina"):
        self.vinculos.append(Vinculo(label,destino))

    def __str__(self) -> str:
        return f"Pagina: {self.nombre}\n----------------------\n{self.contenido}"