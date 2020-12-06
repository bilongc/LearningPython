class MoonCakeMold():
    def __init__(self, shape, color):
        self._shape = shape
        self._color = color

    def to_string(self):
        return self._shape + " " + self._color + " " + \
               str(self.price())

    def price(self):
        if self._shape == 'square':
            return 5
        elif self._shape == 'heart':
            return 6
        else:
            return 3

squareMoonCake = MoonCakeMold('square', 'yellow')
print(squareMoonCake.to_string())

heartMoonCake = MoonCakeMold('heart', 'pink')
print(heartMoonCake.to_string())
