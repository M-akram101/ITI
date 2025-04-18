class Shape:
    def __init__(self, length):
        self.length = length

    def Area(self):
        return 0

    def Perimeter(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self, length)

    def Area(self):
        return self.length * self.length

    def Perimeter(self):
        return self.length * 4


s2 = Shape(7)
s1 = Square(4)
print(s2.Area())
