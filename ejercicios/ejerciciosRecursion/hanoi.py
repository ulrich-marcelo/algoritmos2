def hanoi(n):
    sec = []
    def hanoi_interno(n,origen,inter,fin,secuencia):
        if n==1:
            secuencia += [origen+"-"+fin]
        else:
            hanoi_interno(n-1,origen,fin,inter,secuencia)
            secuencia += [origen+"-"+fin]
            hanoi_interno(n-1,inter,origen,fin,secuencia)
    hanoi_interno(n,"A","B","C",sec)
    print(f"Hanoi de {n} tiene {len(sec)} movimientos: ",sec)

#hanoi(1) = A-C
#haoni(2) = A-B; A-C; B-C
#hanoi(3) = A-C; A-B: C-B; A-C; B-A; B-C; A-C
#hanoi(4) = A-B: A-C: B-C; A-B; C-A; C-B; A-B; A-C; B-C; B-A; C-A; B-C; A-B; A-C; B-C


for i in range(1,10):
    hanoi(i)


