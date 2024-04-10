class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def cumplirAnos(self):
        self.edad+=1

juana = Persona("Juana",20)
print(juana.edad)
juana.cumplirAnos()
print(juana.edad)