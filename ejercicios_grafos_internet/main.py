from internet import Internechi
from navegador import Navegador
from pagina import Pagina





def main():
    internechi = Internechi()
    internechi.agregar_pagina(Pagina("google","Esto es google"))
    internechi.agregar_pagina(Pagina("youtube","Esto es youtube"))
    internechi.agregar_pagina(Pagina("unsam","Esto es unsam"))
    internechi.agregar_pagina(Pagina("github","Esto es github"))
    internechi.agregar_pagina(Pagina("ubuntu","Esto es ubuntu"))
    
    
    navegador = Navegador(internechi)
    navegador.run()


if __name__ == "__main__":
    main()

#Faltaba ir y ver vinculos!!

