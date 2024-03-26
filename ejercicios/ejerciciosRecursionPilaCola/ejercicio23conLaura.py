#definir dos procedimientos, contar_hacia_atras_par y contar_hacia_atras_impar
#con recursion mutua que dado un n, imprima por pantalla todos los numeros de 
#de manera descendiente hasta llegar a uno.

def contar_hacia_atras_par(n):
    print(n)
    contar_hacia_atras_impar(n-1) if n>2 else print(1)

def contar_hacia_atras_impar(n):
    print(n)
    contar_hacia_atras_par(n-1) if n>1 else print(1)

contar_hacia_atras_par(10)










