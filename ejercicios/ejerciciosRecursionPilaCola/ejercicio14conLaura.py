#Definir la funcion esPalindromo, que dada una lista de enteros
# retorne si es o no un palindromo, utilizando recursividad 
#explicita

def esPalindromo(lista):
    if len(lista)==2:
        acum = lista[0] == lista[-1]
        return acum
    elif len(lista)==1:
        return True
    else:
        acum = lista[0] == lista[-1]
        lista.pop(0)
        lista.pop()
    return acum and esPalindromo(lista) 


print(esPalindromo([1,2,3,4,5,4,3,2,1]))

#Forma mati, sin pop

def esPalindromo2(lista):
    if len(lista)<=1:
        return True
    else:
        acum = lista[0] == lista[-1]
        return acum and esPalindromo2(lista[1:-1])

print(esPalindromo2([1,2,3,4,5,4,3,1,1]))
print(esPalindromo2([1,2,3,4,4,3,1,1]))







