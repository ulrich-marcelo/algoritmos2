#Implementar recursion de Fibonacci Pila

def termino_fibonacci_pila(n):
    if n==1 or n==2:
        return 1
    else:
        return termino_fibonacci_pila(n-1) + termino_fibonacci_pila(n-2)

print(termino_fibonacci_pila(6))


def termino_fibonacci_cola(n):
    def fibo_interno(n,acum,acum2):
        if n == 1:
            return acum + acum2
        else:
            aux = acum2
            acum2 += acum
            acum = aux
            return fibo_interno(n-1,acum,acum2)
    return fibo_interno(n,0,1)

print(termino_fibonacci_pila(6))