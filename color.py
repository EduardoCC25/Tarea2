class Color:
  
    def __init__(self, color:str=None):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'Color: {self._color}'

if __name__ == '__main__':
    color1 = Color('red')
    color2 = Color('blue')
    print(color1)
    print(color2)
