class Componente:
    def mostrar(self, nivel=0):
        pass

class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + f"Pieza: {self.nombre}")

class SubConjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"SubConjunto: {self.nombre}")
        for c in self.componentes:
            c.mostrar(nivel + 1)


principal = SubConjunto("Producto Principal")

for i in range(1, 4):
    subconj = SubConjunto(f"SubConjunto {i}")
    for j in range(1, 5):
        subconj.agregar(Pieza(f"Pieza {i}.{j}"))
    principal.agregar(subconj)


opcional = SubConjunto("SubConjunto Opcional")
for j in range(1, 5):
    opcional.agregar(Pieza(f"Pieza O.{j}"))
principal.agregar(opcional)


principal.mostrar()
