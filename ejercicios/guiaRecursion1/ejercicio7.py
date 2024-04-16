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

def decimalBinario(numero : int) -> str:
    residuos = []
    def _decimalBinario(numero):
        if numero != 0:     
            residuo = numero%2
            residuos.insert(0,str(residuo))
            _decimalBinario(numero//2)
    _decimalBinario(numero)
    return "".join(residuos)






print(decimalBinario(16))







