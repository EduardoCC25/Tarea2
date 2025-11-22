from circunferencia import Circunferencia
from cuadrado import Cuadrado
from rectangulo import Rectangulo

def sumar_areas(figuras):
    total = 0
    for figura in figuras:
        total += figura.area()
    return total


def sumar_perimetros(figuras):
    total = 0
    for figura in figuras:
        total += figura.perimetro()
    return total

if __name__ == "__main__":

    try:
        c1 = Cuadrado(lado = 4, color= 'blue')
        c2 = Cuadrado(lado=5)
        
        r1 = Rectangulo(ancho = 5, alto=10, color= 'red')
        r2 = Rectangulo(ancho=8, alto=7)
        
        circ1 = Circunferencia(radio = 8, color = 'red')
        circ2 = Circunferencia(radio = 8)
    except ValueError as e:
        print(f'Error: {e}')

    figuras = [c1,c2,r1,r2, circ1,circ2]

    sum_areas = sumar_areas(figuras)
    sum_perimetros = sumar_perimetros(figuras)
    print(f'\nSuma de los perimetros: {sum_perimetros}\nSuma de las areas: {sum_areas}')
