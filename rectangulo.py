from color import Color
from figurageometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica, Color):
    '''
    Clase que crea objetos de tipo Rectangulo
    '''
    def __init__(self, ancho:float, alto:float, color:str=None):
        FiguraGeometrica.__init__(self, ancho=ancho, alto=alto)
        Color.__init__(self, color=color)

    # def area(self):
    #     return self._ancho * self._alto

    def perimetro(self):
        return 2 * (self._ancho + self._alto)

    def __str__(self):
        return f"Rectangulo: {self.__dict__.__str__()}"

if __name__ == '__main__':
    rec = Rectangulo(ancho=5, alto=6)
    print(rec)
    print(f'Area = {rec.area()}')
    print(f'Perimetro = {rec.perimetro()}')
