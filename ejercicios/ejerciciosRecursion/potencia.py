def potencia(base: int,exp: int):
    if exp == 0:
        return 1
    elif exp<0:
        return potencia(base,exp+1) / base
    else:
        return potencia(base,exp-1)*base
    
print(potencia(2,-3))