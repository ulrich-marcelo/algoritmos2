class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * self.base + 2 * self.altura


rec1 = Rectangulo(1,1)
rec2= Rectangulo(1,2)

print("Areas: ",rec1.area(),rec2.area())
print("Perimetros: ",rec1.perimetro(),rec2.perimetro())
