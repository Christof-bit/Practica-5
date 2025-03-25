import math

class Discriminante:
    def _init_(self, a, b, c):
        self.valor = b**2 - 4 * a * c

    def es_positivo(self):
        return self.valor > 0

    def es_cero(self):
        return self.valor == 0

    def es_negativo(self):
        return self.valor < 0


class Raices:
    def _init_(self, a, b, discriminante):
        self.raiz1 = None
        self.raiz2 = None
        if discriminante.es_positivo() or discriminante.es_cero():
            self.raiz1 = (-b + math.sqrt(discriminante.valor)) / (2 * a)
        if discriminante.es_positivo():
            self.raiz2 = (-b - math.sqrt(discriminante.valor)) / (2 * a)


class EcuacionCuadratica:
    def _init_(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.discriminante = Discriminante(a, b, c)
        self.raices = Raices(a, b, self.discriminante)

    def resolver(self):
        if self.discriminante.es_positivo():
            return f"La ecuación tiene dos raíces {self.raices.raiz1:.5f} y {self.raices.raiz2:.5f}"
        elif self.discriminante.es_cero():
            return f"La ecuación tiene una raíz {self.raices.raiz1:.0f}"
        else:
            return "La ecuación no tiene raíces reales"


def main():
    # Lista de entradas de prueba según el ejemplo proporcionado
    entradas = [(1.0, 3, 1), (2.0, 1, 1), (1, 2, 3)]

    for a, b, c in entradas:
        ecuacion = EcuacionCuadratica(a, b, c)
        print(ecuacion.resolver())


if _name_ == "_main_":
    main()
