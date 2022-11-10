import math

class Areas:
    
    @staticmethod
    def quadrado(lado):
        return lado ** 2
        
    @staticmethod
    def triangulo(base, altura):
        return base * altura / 2
    
    @staticmethod
    def circulo(raio):
        return math.pi * raio ** 2

    @staticmethod
    def retangulo(base, altura):
        return base * altura

    @staticmethod
    def trapezio(baseMenor, baseMaior, altura):
        return (baseMenor + baseMaior) * altura / 2

class Perimetros:
    
    @staticmethod
    def quadrado(lado):
        return lado * 4
    
    @staticmethod
    def circulo(raio):
        return math.pi * raio * 2

    @staticmethod
    def retangulo(base, altura):
        return (base + altura) * 2
