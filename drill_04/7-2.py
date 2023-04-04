class  Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getSymbol(self):
        return self.__symbol

    def setSymbol(self, symbol):
        self.__symbol = symbol

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice

    def setPreviousClosingPrice(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice

    def getCurrentPrice(self):
        return self.__currentPrice

    def setCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice

    def getChangePercent(self):
        return (self.__currentPrice - self.__previousClosingPrice)/self.__previousClosingPrice * 100

    def info(self):
        print('Symbol:{0}, Name:{1}, Previous:{2}, Current:{3}, Change:{4}'.format(self.__symbol, self.__name,
                                                                                   self.__previousClosingPrice,
                                                                                   self.__currentPrice,
                                                                                   self.getChangePercent()))

s = Stock('INTC', 'Intel Co', 20500, 20350)
s.info()