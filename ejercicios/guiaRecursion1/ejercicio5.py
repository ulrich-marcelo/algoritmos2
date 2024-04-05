#Definir una función recursiva potencia que, dados dos números enteros x e y, retorne
#x**y.
import ejercicio4

def potencia_recursiva(x,y):
    if y == 0:
        return 1
    else:
        return x * potencia_recursiva(x,y-1)
    
print(potencia_recursiva(2,3))


def potencia_genuinamente_recursiva(x,y):
    if y == 0:
        return 1
    else:
        return ejercicio4.producto_recursivo(x,potencia_genuinamente_recursiva(x,y-1))
print(potencia_genuinamente_recursiva(2,3))



