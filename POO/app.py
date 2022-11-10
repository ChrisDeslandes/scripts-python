from classes.figuras import *

qua = Quadrado(4)
tri = Triangulo(3,6)
ret = Retangulo(2,8)
tra = Trapezio(3,4,2)

print("Área do quadrado: " + str(qua.getArea()))
print("Perímetro do quadrado: " + str(qua.getPerimetro()))
print("-------------------------------------------------------")
print("Área do triângulo: " + str(tri.getArea()))
print("-------------------------------------------------------")
print("Área do retângulo: " + str(ret.getArea()))
print("Perímetro do retângulo: " + str(ret.getPerimetro()))
print("-------------------------------------------------------")
print("Área do trapézio: " + str(tra.getArea()))

input()
