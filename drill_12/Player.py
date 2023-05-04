class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0

    def inHand(self): # player가 가지고 있는 카드 개수
        return self.N

    def addCard(self, c): # c는 카드 클래스 객체
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.cards.clear()
        self.N = 0

    def value(self): # ace는 1혹은 11로 모두 사용 가능, ACE카드 개수를 세면서
                     # 일단 11로 계산한 후 21이 넘어가면 하나씩 1로 정정
        value = 0
        numofAce = 0
        for i in range(self.inHand()):
            if self.cards[i].getValue() == 1:
                value += 11
                numofAce += 1
            else:
                value += self.cards[i].getValue()
            if numofAce and value > 21:
                numofAce -= 1
                value -= 10
        return value
