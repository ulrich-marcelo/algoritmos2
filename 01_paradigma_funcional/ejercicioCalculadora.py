class Calculadora:
    def __init__(self):
        self.n1 = int(input("Ingrese dos numeros enteros:\nEl primero: "))
        self.n2 = int(input("El segundo: "))
        self.sumar()
        self.dividir()
        self.multiplicar()
        self.dividir()
    def sumar(self):
        print(self.n1 + self.n2)
    def restar(self):
        print(self.n1 - self.n2)
    def multiplicar(self):
        print(self.n1 * self.n2)
    def dividir(self):
        if self.n2 == 0:
            raise ValueError("NO DIVIDAS POR 0 SALAME")
        print(self.n1 / self.n2)

Calculadora()