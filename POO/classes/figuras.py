from classes.entidades import Areas, Perimetros
import math

class Quadrado:
    
    def __init__(self, lado):
        self.lado = lado

    def getArea(self):
        return Areas.quadrado(self.lado)

    def getPerimetro(self):
        return Perimetros.quadrado(self.lado)

class Triangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def getArea(self):
        return Areas.triangulo(self.base, self.altura)

class Retangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def getArea(self):
        return Areas.retangulo(self.base, self.altura)

    def getPerimetro(self):
        return Perimetros.retangulo(self.base, self.altura)

class Trapezio:
    
    def __init__(self, baseMenor, baseMaior, altura):
        self.baseMenor = baseMenor
        self.baseMaior = baseMaior
        self.altura = altura

    def getArea(self):
        return Areas.trapezio(self.baseMenor, self.baseMaior, self.altura)
