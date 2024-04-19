#Definir la función recursiva mcd (máximo común divisor), que dados dos números
#enteros positivos, retorne el máximo común divisor entre ellos.

def divisoresRecursivo(x:int,divisores:list[int]=[],divisor:int=1):
    if int(x/divisor) in divisores:
        divisores.sort()
        return divisores
    else:
        if x%divisor==0:
            divisores.append(divisor)
            divisores.append(int(x/divisor))
        return divisoresRecursivo(x,divisores,divisor+1)
    
print(divisoresRecursivo(15))



def MCD(a, b):
    if a == 0:
        return b
    return MCD(b % a, a)

print(MCD(27,45))













