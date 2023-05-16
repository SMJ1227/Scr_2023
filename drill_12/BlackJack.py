from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *
import random

class BlackJack:
    def __init__(self):
        self.window = Tk()
        self.window.title("Black Jack")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.setupButton()
        self.setupLabel()

        self.player = Player("player")
        self.dealer = Player("dealer")
        self.betMoney = 0
        self.playerMoney = 1000
        self.nCardsDealer = 3
        self.nCardsPlayer = 0
        self.LcardsPlayer = []
        self.LcardsDealer = []
        self.cardDeck = [i for i in range(52)]
        self.deckN = 0 # 카드 덱에서 몇번째 숫자를 선택하느냐 결정하는 변수
        self.window.mainloop()

    def setupButton(self):
        self.B50 = Button(self.window, text='Bet50', width=6, height=1, font=self.fontstyle2, command=self.pressedB50)
        self.B50.place(x=50, y=500)
        self.B10 = Button(self.window, text="Bet 10", width=6, height=1, font=self.fontstyle2, command=self.pressedB10)
        self.B10.place(x=150, y=500)
        self.B1 = Button(self.window, text="Bet 1", width=6, height=1, font=self.fontstyle2, command=self.pressedB1)
        self.B1.place(x=250, y=500)
        self.Hit = Button(self.window, text="Hit", width=6, height=1, font=self.fontstyle2, command=self.pressedHit)
        self.Hit.place(x=400, y=500)
        self.Stay = Button(self.window, text="Stay", width=6, height=1, font=self.fontstyle2, command=self.pressedStay)
        self.Stay.place(x=500, y=500)
        self.Deal = Button(self.window, text="Deal", width=6, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=600, y=500)
        self.Again = Button(self.window, text="Again", width=6, height=1, font=self.fontstyle2, command=self.pressedAgain)
        self.Again.place(x=700, y=500)
        self.Hit['state'] = 'disabled'
        self.Hit['bg'] = 'gray'
        self.Stay['state'] = 'disabled'
        self.Stay['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def pressedB50(self):
        if 50 <= self.playerMoney:
            PlaySound('sounds/chip.wav', SND_FILENAME)
            self.betMoney += 50
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= 50
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"

    def pressedB10(self):
        if 10 <= self.playerMoney:
            PlaySound('sounds/chip.wav', SND_FILENAME)
            self.betMoney += 10
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= 10
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"

    def pressedB1(self):
        if 1 <= self.playerMoney:
            PlaySound('sounds/chip.wav', SND_FILENAME)
            self.betMoney += 1
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= 1
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"

    def pressedHit(self):
        self.nCardsPlayer += 1
        self.hitPlayer(self.nCardsPlayer) # 새로운 위치에 카드 추가 생성
        if self.player.value() > 21:
            self.checkWinner()
            self.Hit['state'] = 'disabled'
            self.Hit['bg'] = 'gray'
            self.Stay['state'] = 'disabled'
            self.Stay['bg'] = 'gray'
            self.Again['state'] = 'active'
            self.Again['bg'] = 'white'

    def hitPlayer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player.addCard(newCard)
        p = PhotoImage(file='cards/'+newCard.filename())
        self.LcardsPlayer.append(Label(self.window, image=p))
        self.LcardsPlayer[self.player.inHand()-1].image = p
        self.LcardsPlayer[self.player.inHand()-1].place(x=250+n*30, y=350)
        self.LPlayerPts.configure(text=str(self.player.value()))
        PlaySound('sound/cardFlip1.wav', SND_FILENAME)

    def hitDealerDown(self):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file='cards/b2fv.png')
        self.LcardsDealer.append(Label(self.window, image=p))
        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=250, y=150)

    def hitDealer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file='cards/' + newCard.filename())
        self.LcardsDealer.append(Label(self.window, image=p))
        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=250+n*30, y=150)

    def checkWinner(self):
        # 뒤집힌 카드를 다시 그린다.
        p = PhotoImage(file="cards/" + self.dealer.cards[0].filename())
        self.LcardsDealer[0].configure(image=p)  # 이미지 레퍼런스 변경
        self.LcardsDealer[0].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LdealerPts.configure(text=str(self.dealer.value()))

        if self.player.value() > 21:
            self.Lstatus.configure(text="Player Busts")
            PlaySound('sounds/wrong.wav', SND_FILENAME)
        elif self.dealer.value() > 21:
            self.Lstatus.configure(text="Dealer Busts")
            self.playerMoney += self.betMoney * 2
            PlaySound('sounds/win.wav', SND_FILENAME)
        elif self.dealer.value() == self.player.value():
            self.Lstatus.configure(text="Push")
            self.playerMoney += self.betMoney
        elif self.dealer.value() < self.player.value():
            self.Lstatus.configure(text="You won!!")
            self.playerMoney += self.betMoney * 2
            PlaySound('sounds/win.wav', SND_FILENAME)
        else:
            self.Lstatus.configure(text="Sorry you lost!")
            PlaySound('sounds/wrong.wav', SND_FILENAME)
        self.betMoney = 0
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.LbetMoney.configure(text="$" + str(self.betMoney))

    def pressedStay(self):
        while self.dealer.value() < 17:
            self.nCardsDealer += 1
            self.hitDealer(self.nCardsDealer)
        self.checkWinner()
        self.Hit['state'] = 'disabled'
        self.Hit['bg'] = 'gray'
        self.Stay['state'] = 'disabled'
        self.Stay['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'

    def deal(self):
        self.player.reset()
        self.dealer.reset()
        random.shuffle(self.cardDeck)
        self.deckN = 0 # 카드 덱에서 가져올 카드 인덱스 초기화
        self.hitPlayer(0) # 첫번째 카드를 0번 위치에 생성
        self.hitPlayer(1) # 두번째 카드를 1번 위치에 생성
        self.nCardsPlayer = 1 # 플레이어의 현재 카드 위치는 1번
        self.hitDealerDown() # 첫번째 딜러 카드는 뒤집어서 생성
        self.hitDealer(1) # 두번째 딜러 카드는 0번 위치에 생성
        self.nCardsDealer = 0

    def pressedDeal(self):
        self.deal()
        self.Hit['state'] = 'active'
        self.Hit['bg'] = 'white'
        self.Stay['state'] = 'active'
        self.Stay['bg'] = 'white'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.B50['state'] = 'disabled'
        self.B50['bg'] = 'gray'
        self.B10['state'] = 'disabled'
        self.B10['bg'] = 'gray'
        self.B1['state'] = 'disabled'
        self.B1['bg'] = 'gray'

    def pressedAgain(self):
        # 딜러와 플레이어 카드 라벨 이미지 삭제
        for i in range(self.dealer.inHand()):
            self.LcardsDealer[i].configure(bg='green', image='')
        for i in range(self.player.inHand()):
            self.LcardsPlayer[i].configure(bg='green', image='')
        self.LcardsDealer.clear()
        self.LcardsPlayer.clear()
        self.LdealerPts.configure(text="")
        self.LPlayerPts.configure(text="")
        self.Lstatus.configure(text="")

        self.B50['state'] = 'active'
        self.B50['bg'] = 'white'
        self.B10['state'] = 'active'
        self.B10['bg'] = 'white'
        self.B1['state'] = 'active'
        self.B1['bg'] = 'white'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def setupLabel(self):
        self.LbetMoney = Label(text='$0', width=4, height=1, font=self.fontstyle, bg='green', fg='cyan')
        self.LbetMoney.place(x=130, y=450)
        self.LplayerMoney = Label(text='You have $1000', width=15, height=1, font=self.fontstyle, bg='green', fg='cyan')
        self.LplayerMoney.place(x=450, y=450)
        self.LPlayerPts = Label(text='', width=2, height=1, font=self.fontstyle2, bg='green', fg='white')
        self.LPlayerPts.place(x=300, y=300)
        self.LdealerPts = Label(text='', width=2, height=1, font=self.fontstyle2, bg='green', fg='white')
        self.LdealerPts.place(x=300, y=100)
        self.Lstatus = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lstatus.place(x=500, y=300)

BlackJack()
