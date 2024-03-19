def longitud_recursiva(lista,count=0):
    if not lista:
        return count
    else:
        return longitud_recursiva(lista[1:],count+1)
    
def longitud_iterativa(lista):
    count = 0
    while lista:
        count+=1
        lista.pop()
    return count



print(longitud_recursiva([1,2,3,4]))
print(longitud_iterativa([1,2,3,4]))




