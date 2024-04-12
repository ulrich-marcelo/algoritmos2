#Fibonacci con recursion de Cola
#Para ello hago pila explicita, asi no uso la pila de ejecucion
#Pila: 1. saco tope, 2. pusheo fib 3. if 0 o 1 sumo acum

def fibonacci(n:int)-> int:
    def fibo_interna(pila:list[int],acum:int = 0)->int:
        
        if not pila:
            return acum
        else:
            actual = pila.pop()
            if actual<2:
                acum +=actual
            else:
                pila.append(actual-1)
                pila.append(actual-2)  
            return fibo_interna(pila,acum)                

    return fibo_interna([n])

print(fibonacci(4))

#Ahora con programacion dinamica: asi no calculamos las cosas dos veces

def fibonacci2(n:int)->int:
    mem = {}
    def fibo(n:int)->int:
        if n<= 1:
            return n
        else:
            if not n in mem:
                mem[n] = fibo(n-2) + fibo(n-1)
            return mem[n]
    return fibo(n)
print(fibonacci2(4))
                

        






