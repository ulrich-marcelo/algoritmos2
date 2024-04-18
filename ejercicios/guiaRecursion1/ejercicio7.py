'''
Definir los siguiente:
a) Una función recursiva decimalBinario que, dado un número decimal, retorne
el mismo en base binaria.
b) Una función recursiva cambioBaseDecimal que, dado un número decimal n y
un entero b, retorne la conversión del número n en base b.
c) Una función unosBinario que, dado un número binario (100101), retorne un
entero indicando la cantidad de 1s que tiene el mismo. El parámetro de la función
puede ser un entero que respete el formato binario (sólo acepte 0s y 1s).
d) Una función binarioDecimal que, dado un número binario (100101), retorne el
mismo número en base decimal (37).
'''
from functools import reduce

def decimalBinario(numero : int) -> str:
    residuos = []
    def _decimalBinario(numero):
        if numero != 0:     
            residuo = numero%2
            residuos.insert(0,str(residuo))
            _decimalBinario(numero//2)
    _decimalBinario(numero)
    return "".join(residuos)

def cambioBaseDecimal(numero:int,b:int)->str:
    if not (b <=36 and b>=2):
        raise ValueError("FLACO PONE UNA BASE VALIDA")
    residuos = []
    def _cambio(num:int):
        if num!=0:
            residuo = num%b
            if residuo>=10:
                residuo = chr(residuo+55)
            residuos.insert(0,str(residuo))
            _cambio(num//b)
    _cambio(numero)
    return ''.join(residuos)

def unosBinario(binario : str)->int:
    def es_binario(bina:str)->bool:
        return bool(reduce(lambda x,y: x*y,map(lambda x: x=='1' or x=='0',bina),True))

    if not es_binario(binario):
        raise ValueError("El valor ingresado no es un string binario!!")
    return reduce(lambda x,y: int(x)+int(y),binario,0)

def binarioDecimal(binario:str)->int:
    return 0

print(decimalBinario(16))
print(cambioBaseDecimal(178,36))
print(unosBinario('10101110111'))








