def suma_primero(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + resta_primero(lista[1:])
    
def resta_primero(lista):
    if len(lista) == 1:
        return - lista[0]
    else:
        return - lista[0] + suma_primero(lista[1:])

lista = [1,2,3,4,5]
print(resta_primero(lista))