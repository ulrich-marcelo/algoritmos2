from dataclasses import dataclass

@dataclass
class Player:
    nombre : str
    pata_cm : float
    def dar_paso(self,distancia_inicial:float)->float:
        return distancia_inicial - self.pata_cm



class PanQueso:
    def __init__(self,p1: Player,p2: Player,dist_cm: float):
        self.p1 = p1
        self.p2 = p2
        if dist_cm < 0:
            raise ValueError ("Salame te confundiste, la distancia tiene que ser mayor a 0.")
        self.dist_cm = dist_cm
        self.gana = None
    def jugar(self) ->None:
        self.jugar_p1()

    def jugar_p1(self):
        if self.dist_cm < self.p1.pata_cm:
            self.gana = self.p1
        else:
            self.dist_cm -= self.p1.pata_cm
            self.jugar_p2()
    def jugar_p2(self):
        if self.dist_cm < self.p2.pata_cm:
            self.gana = self.p2
        else:
            self.dist_cm -= self.p2.pata_cm
            self.jugar_p1()


    def resultado(self):
        if self.gana is None:
            return "Juego sin comenzar"
        else:
            return f"Gano player {self.gana}"


if __name__ == "__main__":
    p1 = Player("Juana",33.6)
    p2 = Player("Laura",22.5)

    juego = PanQueso(p1,p2,355)
    print(juego.resultado())
    juego.jugar()
    print(juego.resultado())