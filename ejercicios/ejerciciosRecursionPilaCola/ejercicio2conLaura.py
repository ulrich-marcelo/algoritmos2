#definir desde_hasta con recursion de cola. dados dos 
#ints devuelva lista de num consecutivos, el primero va

def desde_hasta(n1 : int, n2 : int)->list[int]:
    def desde_hasta_interno(desde : int,hasta : int,acum : list[int]):
        if desde == hasta:
            acum.append(desde)
            return acum
        else: 
            acum.append(desde)
            return desde_hasta_interno(desde + 1, hasta,acum )
    return [] if n1>n2 else desde_hasta_interno(n1 + 1,n2,[n1])

print(desde_hasta(1,5))

