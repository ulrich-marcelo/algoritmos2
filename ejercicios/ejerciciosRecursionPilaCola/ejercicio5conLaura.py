#Implementar una version con recursion de cola que produzca:
#suma_resta_alternada([1,2,3,4,5]) = 1+2-3+4-5

def suma_resta_alternada(lista):
    def suma_resta_alternada_interna(lista_interna,suma,indice):
        if len(lista_interna)==0:
            return suma
        else:
            indice_par = indice % 2 == 0
            coef = -1 if indice_par else 1
            suma += coef * lista_interna[0]
            indice +=1
            return suma_resta_alternada_interna(lista_interna[1:],suma,indice)
    return suma_resta_alternada_interna(lista[1:],lista[0],1)
print(suma_resta_alternada([1,2,3,4,5,6]))

#Forma con dos funciones internas, recursiva posta, 
#la mia roza lo iterativo

def s_r_alt(xs):
    if not xs:
        return 0
    else:
        acum = xs[0]
        def suma(xs,acum):
            if not xs:
                return acum
            else:
                acum +=xs[0]
                return resta(xs[1:],acum)
        def resta(xs,acum):
            if not xs:
                return acum
            else:
                acum -= xs[0]
                return suma(xs[1:],acum)
    return suma(xs[1:],acum)

print(s_r_alt([1,2,3,4,5,6]))

#Mejorandola

def suma_resta_acumulada_mejor(lista):
    def suma(xs,acum):
        if not xs:
            return acum
        else:
            acum += xs[0]
            return resta(xs[1:],acum)
    def resta(xr,acum):
        if not xr:
            return acum
        else:
            acum -= xr[0]
            return suma(xr[1:],acum)
    return suma(lista[1:],lista[0])

print(suma_resta_acumulada_mejor([1,2,3,4,5]))


