from tkinter import *
import random

class MainGUI:
    def __init__(self):
        window = Tk()
        window.title("Tic-Tac-Toe")
        frame = Frame(window)
        frame.pack()
        self.imageX = PhotoImage(file='pybook/image/x.gif')
        self.imageO = PhotoImage(file='pybook/image/o.gif')
        self.imageE = PhotoImage(file='pybook/image/empty.gif')
        self.matrix = []
        self.done = False # 게임 종료 여부
        self.turn = True # True = X, False = O, 턴 제어 변수
        self.count = 0 # 턴 수 세기
        for i in range(3):
            self.matrix.append([])
            for j in range(3):
                self.matrix[i].append(Button(frame, image=self.imageE, text=' ',
                                             command=lambda row=i, col=j: self.pressed(row, col)))
                self.matrix[i][j].grid(row=i, column=j)
        self.explain = StringVar()
        self.explain.set('플레이어 X차례')
        self.label = Label(window, textvariable=self.explain).pack()
        Button(window, text='다시생성', command=self.refresh).pack()
        window.mainloop()

    def refresh(self):
        for i in range(3):
            for j in range(3):
                self.matrix[i][j]['image'] = self.imageE
                self.matrix[i][j]['text'] = ' '
        self.done = False
        self.turn = True
        self.count = 0
        self.explain.set('플레이어 X차례')

    def pressed(self, row, col):
        if not self.done and self.matrix[row][col]['text'] == ' ':
            if self.turn:
                self.matrix[row][col]['image'] = self.imageX
                self.matrix[row][col]['text'] = 'X'
            else:
                self.matrix[row][col]['image'] = self.imageO
                self.matrix[row][col]['text'] = 'O'
            self.turn = not self.turn
            if self.check() != ' ':
                self.done = True
                self.explain.set(self.check()+'가 이겼습니다.')
            elif self.turn:
                self.explain.set('플레이어 X차례')
            else:
                self.explain.set('플레이어 O차례')
        self.count += 1
        if not self.done and self.count == 9:
            self.explain.set('비겼습니다.')

    def check(self):
        for i in range(3):
            ch = self.matrix[i][0]['text'] # 같은 행
            if ch != ' ' and ch == self.matrix[i][1]['text'] and ch == self.matrix[i][2]['text']:
                return ch
            ch = self.matrix[0][i]['text'] # 같은 열
            if ch != ' ' and ch == self.matrix[1][i]['text'] and ch == self.matrix[2][i]['text']:
                return ch
        ch = self.matrix[0][0]['text'] # 대각선
        if ch != ' ' and ch == self.matrix[1][1]['text'] and ch == self.matrix[2][2]['text']:
            return ch
        ch = self.matrix[0][2]['text']  # 대각선
        if ch != ' ' and ch == self.matrix[1][1]['text'] and ch == self.matrix[2][0]['text']:
            return ch
        return ' '


MainGUI()
