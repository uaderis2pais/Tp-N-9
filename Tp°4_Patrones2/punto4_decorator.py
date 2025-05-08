class Numero:
    def __init__(self, valor):
        self.valor = valor

    def operar(self):
        return self.valor

class Decorador:
    def __init__(self, componente):
        self.componente = componente

    def operar(self):
        return self.componente.operar()

class Sumar2(Decorador):
    def operar(self):
        return self.componente.operar() + 2

class Multiplicar2(Decorador):
    def operar(self):
        return self.componente.operar() * 2

class Dividir3(Decorador):
    def operar(self):
        return self.componente.operar() / 3

#ejemplo de uso

base = Numero(9)
print("Original:", base.operar())
print("Suma 2:", Sumar2(base).operar())
print("Multiplica por 2:", Multiplicar2(base).operar())
print("Divide por 3:", Dividir3(base).operar())


resultado = Dividir3(Multiplicar2(Sumar2(base)))
print("Anidado:", resultado.operar())
