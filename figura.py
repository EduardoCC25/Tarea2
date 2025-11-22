from abc import ABC


class FiguraGeometrica(ABC):
  
    def __init__(self, ancho:float, alto:float):
        if ancho <= 0 or alto <= 0:
            raise ValueError('El ancho o alto no puede ser menor o igual que cero.')
        else:
            self._ancho = ancho
            self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if ancho <= 0:
            raise ValueError('El ancho no puede ser menor o igual que cero.')
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if alto <= 0:
            raise ValueError('El alto no puede ser menor o igual que cero.')
        self._alto = alto

    def area(self):
        return self._ancho * self._alto

    def perimetro(self):
        pass

if __name__ == '__main__':
    fg1 = FiguraGeometrica(ancho=5, alto=6)
    print(fg1)
    print(f'Area: {fg1.area()}')
    print(f'Perimetro: {fg1.perimetro()}')
