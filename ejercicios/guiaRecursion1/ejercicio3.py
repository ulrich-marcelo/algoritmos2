#Definir una función recursiva fibonacci que, dado un entero n, retorne el n-ésimo
#término de la sucesión de Fibonacci (1, 1, 2, 3, 5, 8, 13, ...)

def termino_fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return termino_fibonacci(n-1) + termino_fibonacci(n-2)

print(termino_fibonacci(10))









