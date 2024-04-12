'''
Pensando una representación simplificada de un laberinto, 
les propongo definir una estructura que permita modelar 
un laberinto cuadrado. La construcción del laberinto 
podría pensarse así:

1. Generar un cuadrado con todas las posiciones 
(por ejemplo, 5x5 o 10x10, etc) donde cada posición 
sea un muro. Inicialmente, el laberinto no tiene recorrido alguno.

2. Definir como entrada la posición de arriba a la 
izquierda y la salida sería abajo a la derecha.

3. Construir al menos un camino utilizando el concepto 
de backtracking donde comenzamos desde la entrada e 
iremos tirando muros en un recorrido aleatorio hasta llegar 
a la salida. Imaginemos este proceso como el de una 
lombriz que va generando surcos en la tierra.

Finalmente, implementar una operación que permita encontrar 
todos los caminos posibles desde la entrada hasta 
la salida del laberinto.
'''


def armar_un_cuadrado(tamano :int) -> list[list[int]]:
    lista = []
    for i in range(tamano):
        lista_interna = [j+(tamano*i+1) for j in range(tamano)]
        lista.append(lista_interna.copy())
    return lista

print(armar_un_cuadrado(4))

#Como lo hizo tomi?
#Lo hizo tomi con mucho codigo


