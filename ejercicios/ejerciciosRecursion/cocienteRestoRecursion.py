
def cociente(dividendo,divisor):
    if divisor ==0:
        raise ValueError("Como vas a dividir por cero!!")
    else:
        if dividendo >=divisor:
            return divisor + cociente(dividendo-divisor,divisor) 
        else:
            return 0


    
def resto(dividendo,divisor):
    if divisor ==0:
        raise ValueError("Como vas a dividir por cero!!")
    else:
        if dividendo >=divisor:
            return resto(dividendo-divisor,divisor) 
        else:
            return dividendo

print(cociente(12,2),resto(12,2))
print(cociente(13,2),resto(13,2))
print(cociente(14,2),resto(14,2))