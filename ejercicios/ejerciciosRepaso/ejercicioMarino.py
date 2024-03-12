class Marino():
    def __init__(self):
        pass
    def hablar(self):
        print("Hola, soy un animal marino!")

class Pulpo(Marino):
    def hablar(self):
        print("Hola, soy un pulpo!")

class Foca(Marino):
    def __init__(self,mensaje):
        super().__init__()
        self.mensaje = mensaje
    def hablar(self):
        print(self.mensaje)

pez = Marino()
pez.hablar()

pulpi = Pulpo()
pulpi.hablar()

foqui = Foca("ESCUCHEn, CORRAN LA BOLA, SE HICIERON PUTOS LOS NEGROS DE CASANOVA")
foqui.hablar()