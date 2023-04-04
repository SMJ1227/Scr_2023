SLOW = 1
MEDIUM = 2
FAST = 3

class Fan:
    def __init__(self, speed=SLOW, radius=5, color='Blue', on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def setspeed(self):
        return self.__speed

    def getspeed(self, speed):
        self.__speed = speed

    def setradius(self):
        return self.__radius

    def getradius(self, radius):
        self.__radius = radius

    def setcolor(self):
        return self.__color

    def getcolor(self, color):
        self.__color = color

    def seton(self):
        return self.__on

    def geton(self, on):
        self.__on = on

    def info(self):
        print('Speed:{0}, Radius:{1}, Color:{2}, On:{3}'.format(self.__speed, self.__radius, self.__color, self.__on))


fan1 = Fan(FAST, 10, 'Yellow', True)
fan2 = Fan(MEDIUM, 5, 'Blue', False)

fan1.info()
fan2.info()
