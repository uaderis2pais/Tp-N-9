class Laminador:
    def producir(self):
        pass

class Tren5mts(Laminador):
    def producir(self):
        return "Lámina de 5 metros producida."

class Tren10mts(Laminador):
    def producir(self):
        return "Lámina de 10 metros producida."

class Lamina:
    def __init__(self, tren):
        self.tren = tren

    def producir(self):
        print(self.tren.producir())


