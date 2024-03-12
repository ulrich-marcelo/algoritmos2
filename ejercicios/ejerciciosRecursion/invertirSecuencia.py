def invertir_secuencia(sec: str):
    return sec[-1] + invertir_secuencia(sec[0:len(sec)-1]) if len(sec)>0 else ''

print(invertir_secuencia('hola'))