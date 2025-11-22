from color import Color
from figurageometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica, Color):
  
    def __init__(self, lado:float, color:str=None):
        FiguraGeometrica.__init__(self, ancho=lado, alto=lado)
        Color.__init__(self, color=color)

    def perimetro(self):
        return 4 * self._ancho

if __name__ == '__main__':
    c1 = Cuadrado(lado=5, color='red')
    print(c1)
    print(f'Area = {c1.area()}')
    print(f'Perimetro = {c1.perimetro()}')
    print(Cuadrado.mro())
