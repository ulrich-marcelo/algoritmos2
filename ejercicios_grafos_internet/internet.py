from pagina import Pagina


class Internechi:
    def __init__(self) -> None:
        self.paginas : dict[str,Pagina] = {}

    def agregar_pagina(self,pagina:Pagina)->None:
        self.paginas[pagina.nombre]=pagina

    def obtener_pagina(self,nombre:str)->Pagina:
        if nombre not in self.paginas:
            raise ValueError("ERROR 404: Page not found.")
        return self.paginas[nombre]
    

    