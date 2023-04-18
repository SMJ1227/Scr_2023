from tkinter import *
import random
import tkinter.messagebox

class MainGUI:
    def __init__(self):
        window = Tk()
        window.title('24점게임')
        Button(window, text='새로고침', command=self.refresh).pack()
        frame1 = Frame(window)
        frame1.pack()
        self.deck = [i for i in range(52)]
        random.shuffle(self.deck)
        self.imagelist = []
        self.labellist = []
        for i in range(4):
            self.imagelist.append(PhotoImage(file='card/'+str(self.deck[i]+1)+'.gif'))
            self.labellist.append(Label(frame1, image=self.imagelist[i]))
            self.labellist[i].pack(side=LEFT)

        frame2 = Frame(window)
        frame2.pack()
        Label(frame2, text='수식을 입력하세요').pack(side=LEFT)
        self.e = Entry(frame2)
        self.e.pack(side=LEFT)
        Button(frame2, text='확인', command=self.verify).pack(side=LEFT)

        window.mainloop()

    def refresh(self):
        random.shuffle(self.deck)
        for i in range(4):
            self.imagelist[i] = PhotoImage(file='card/' + str(self.deck[i] + 1) + '.gif')
            self.labellist[i]['image'] = self.imagelist[i]

    def verify(self):
        fourCards = [self.deck[i]%13+1 for i in range(4)]
        expression = self.e.get()
        expression = expression.replace('(', ' ')
        expression = expression.replace(')', ' ')
        expression = expression.replace('+', ' ')
        expression = expression.replace('-', ' ')
        expression = expression.replace('*', ' ')
        expression = expression.replace('/', ' ')
        numbers = [eval(s) for s in expression.split()]
        fourCards.sort()
        numbers.sort()
        if fourCards == numbers:
            if eval(self.e.get()) == 24:
                tkinter.messagebox.showinfo('정답', '정답')
            else:
                tkinter.messagebox.showinfo('틀림', self.e.get()+'은 24가 아니다.')
        else:
            tkinter.messagebox.showinfo('틀림', '보여지는 카드를 사용해야합니다')


MainGUI()
