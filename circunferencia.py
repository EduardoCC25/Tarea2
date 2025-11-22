import math

from color import Color
from figurageometrica import FiguraGeometrica


class Circunferencia(FiguraGeometrica, Color):
  
    def __init__(self,radio:float, color:str=None):
        FiguraGeometrica.__init__(self, ancho=radio, alto=1)
        Color.__init__(self, color=color)

    def __str__(self):
        return f'Circunferencia(radio={self.ancho})'

    def area(self):
        return math.pi * self._ancho * self._ancho

    def perimetro(self):
        return 2 * math.pi * self._ancho

if __name__ == '__main__':
    circ = Circunferencia(radio=5)
    print(circ)
    print(f'Area = {circ.area()}')
    print(f'Perimetro = {circ.perimetro()}')
