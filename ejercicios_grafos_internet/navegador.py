from pagina import Pagina
from internet import Internechi
from entrada_consola import EntradaConsola
from salida_consola import SalidaConsola




class Navegador:
    
    def __init__(self,web:Internechi) -> None:
        #TODO Historial
        #self.historial = Historial()
        self.home : Pagina = Pagina("HOME","HOME MI NAVEGADOR")
        self.pagina_actual : Pagina = self.home
        
        self.salida = SalidaConsola()
        self.web = web
        self.operaciones = {
            "abrir":self.abrir_pagina,
            "ir":self.ir_vinculo,
            "cerrar":self.cerrar,
            "atras":self.atras,
            "adelante":self.adelante
        }
        self.entrada = EntradaConsola(self.operaciones)

    def set_home(self,nombre:str):
        try:
            self.home = self.web.obtener_pagina(nombre)
        except ValueError:
            raise ValueError("Pagina Inexistente")

    def abrir_pagina(self,nombre:str):
        try:
            self.pagina_actual = self.web.obtener_pagina(nombre[0])
            self.salida.mostrar(self.pagina_actual)
        except ValueError:
            self.salida.mostrar_error("Pagina no encontrada")

    def ir_vinculo(self):
        pass

    def cerrar(self):
        pass

    def atras(self):
        pass

    def adelante(self):
        pass

    def run(self):
        comando = ""
        self.salida.mostrar(self.pagina_actual)
        while comando != "cerrar":
            try:
                comando,args = self.entrada.leer()
                self.operaciones[comando](args)
            except ValueError as e:
                self.salida.mostrar_error(e)















