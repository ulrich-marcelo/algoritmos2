"""Definir funciones recursivas cociente y resto que, a partir de dos números enteros,
retorne el cociente y el resto entre ellos respectivamente, a partir de la técnica de restas
sucesivas. Expresar cuál sería el orden bien fundado entre los elementos del dominio
para esta función."""

def cociente_recursivo(x,y):
    if x<y:
        return 0
    else:
        return 1 + cociente_recursivo(x-y,y)

def resto_recursivo(x,y):
    if x<y:
        return

print(cociente_recursivo(6,2))
print(cociente_recursivo(6,4))
print(cociente_recursivo(18,5))
