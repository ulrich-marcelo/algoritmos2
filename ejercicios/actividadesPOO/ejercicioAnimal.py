#Animales que hereden y modifiquen Animal, deberia ser una interfaz
class Animal:
    def __init__(self): 
        pass
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print("Guau")

class Gato(Animal):
    def hablar(self):
        print("miau")

perro = Perro()
gato = Gato()
perro.hablar()
gato.hablar()