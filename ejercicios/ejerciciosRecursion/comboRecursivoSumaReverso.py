'''Definir lo siguiente:

    a. Una función recursiva digitos, que dado un número entero, retorne su cantidad de dígitos.
    b. Una función recursiva reversa_num que, dado un número entero, retorne su imagen especular. Por ejemplo: reversa_num(345) = 543
    c. Una función recursiva suma_digitos que, dado un número entero, retorne la suma de sus dígitos.
    d. Una función recursiva que retorne los dos valores anteriores a la vez como un par, aprovechando la recursión.
'''

#a
def digitos(n: int)-> int:
    if n<10:
        return 1
    else:
        return 1 + digitos(n//10)

#b
def reversa_num(n:int) -> int:
    if n<10:
        return n
    else:
        potencia = 10 ** (digitos(n)-1)
        primer_digito = n // potencia
        valor_previo = reversa_num (n- primer_digito * potencia)
        return valor_previo * 10 + primer_digito

#otra opcion
def reversa_num2(n:int)->int:
    if n<10:
        return n
    else:
        potencia = 10 ** (digitos(n)-1)
        ultimo = n%10
        valor_previo = reversa_num2(n//10)
        return potencia * ultimo + valor_previo

#c
def suma_digitos(n:int)->int:
    if n<10:
        return n
    else:
        return n%10+suma_digitos(n//10)


#d
def rev_sum(n:int) -> tuple[int,int]:
    if n<10:
        return (n,n)
    else:
        ultimo = n%10
        reverso_previo,suma_previa = rev_sum(n//10)
        potencia = 10 ** (digitos(n)-1)
        reverso = potencia * ultimo + reverso_previo
        
        suma = suma_previa + ultimo
        return(reverso,suma)


if __name__ == "__main__":
    print(rev_sum(1234))




