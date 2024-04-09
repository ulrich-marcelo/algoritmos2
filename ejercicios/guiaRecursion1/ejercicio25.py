import time
def todosConTodos(lista1,lista2):
    listaPares = []
    for i in lista1:
        for j in lista2:
            listaPares.append([i,j])
    return listaPares
start = time.time()
print(todosConTodos([1,2,3],[4,5,6]))
end = time.time()
print(end-start)





def todosConTodosRecursivo(lista1,lista2):
    if len(lista1)==0:
        return []
    elif len(lista2)==0:
        return[]
    else:
        inicial = lista1.pop(0)
        return [(inicial,i) for i in lista2] + todosConTodosRecursivo(lista2,lista1)

start2 = time.time()
print(todosConTodosRecursivo([1,2,3],[4,5,6,7]))
end2 = time.time()
print(end2-start2)






