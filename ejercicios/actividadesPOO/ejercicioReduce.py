from functools import reduce
lista = [1,2,3,4]
prod = reduce(lambda x,y: x*y,lista)
print(prod)