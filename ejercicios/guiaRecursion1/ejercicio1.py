#1. Definir una función recursiva sumatoria que, dado un entero n, 
#retorne el resultado de la suma 1+2+3+...+(n-1)+n.

def sumatoria_recursiva(n):
    def sumatoria_recursiva_interna(n,acum):
        if n == 1:
            return acum + 1
        else:
            acum+=n 
            return sumatoria_recursiva_interna(n-1,acum)
    return sumatoria_recursiva_interna(n,0)

#print(sumatoria_recursiva(5))

#2.Definir una función recursiva factorial que, 
#dado un número entero positivo, retorne el factorial 
#de ese número.

def factorial_recursivo(n):
    if n ==1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

#print(factorial_recursivo(4)) 













