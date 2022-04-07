import math

# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
def areaTriangulo( base, altura ) :
    return base * altura / 2;

def areaCirculo( radio ) :
    return math.pi * radio ** 2;

base = 14
altura = 10
triangulo = areaTriangulo( base, altura )
print( f'El área del triángulo de base: { base }m y altura: { altura }m \nes de { triangulo }m2\n' )

radio = 3
circulo = areaCirculo( radio )
print( f'El área del círculo de radio { radio }m \nes de: { round( circulo, 2 ) }m2\n' )