class GeomatricObject:
    def __init__(self, color):
        self.color = color

class Triange(GeomatricObject):
    def __init__(self, side1, side2, side3, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        #super().__init__(color)
        GeomatricObject.__init__(self, color)

    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s-self.side1) * (s-self.side2) * (s-self.side3)) ** 0.5

    def getPerimeter(self):
        return self.side3 + self.side2 + self.side1

    def __str__(self):
        return 'Triange side1:{0}, side2:{1}, side:{2}, side:{3:.2f}, perimeter:{4}'.format(self.side1,
            self.side2, self.side3, self.getArea(), self.getPerimeter())

t = Triange(3, 4, 5, 'red')
print(t.__str__())
#print(t)
