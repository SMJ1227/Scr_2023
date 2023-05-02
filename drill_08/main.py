from tkinter import *
import random


class MainGUI:
    def __init__(self):
        window = Tk()
        window.title("사목게임")
        frame = Frame(window)
        frame.pack()
        self.imageX = PhotoImage(file='pybook/image/x.gif')
        self.imageO = PhotoImage(file='pybook/image/o.gif')
        self.imageE = PhotoImage(file='pybook/image/empty.gif')
        self.matrix = []
        self.done = False  # 게임 종료 여부
        self.turn = True  # True = 빨간색, False = 노란색, 턴 제어 변수
        self.count = 0  # 턴 수 세기
        for i in range(6):
            self.matrix.append([])
            for j in range(7):
                self.matrix[i].append(Button(frame, image=self.imageE, text=' ',
                                             command=lambda row=i, col=j: self.pressed(row, col)))
                self.matrix[i][j].grid(row=i, column=j)
        self.explain = StringVar()
        self.explain.set('플레이어 X차례')
        self.label = Label(window, textvariable=self.explain).pack()
        Button(window, text='다시생성', command=self.refresh).pack()
        window.mainloop()

    def refresh(self):
        for i in range(6):
            for j in range(7):
                self.matrix[i][j]['image'] = self.imageE
                self.matrix[i][j]['text'] = ' '
        self.done = False
        self.turn = True
        self.count = 0
        self.explain.set('플레이어 X차례')

    def pressed(self, row, col):
        row = self.findrow(col)
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
                self.explain.set(self.check() + '가 이겼습니다.')
            elif self.turn:
                self.explain.set('플레이어 X차례')
            else:
                self.explain.set('플레이어 O차례')
        self.count += 1
        if not self.done and self.count == 42:
            self.explain.set('비겼습니다.')

    def check(self):
        # 가로 4개 체크
        for i in range(6):
            for j in range(4):
                player = self.matrix[i][j]['text']
                if player != ' ' \
                        and player == self.matrix[i][j+1]['text'] \
                        and player == self.matrix[i][j+2]['text'] \
                        and player == self.matrix[i][j+3]['text']:
                    return player
        # 세로 4개 체크
        for i in range(3):
            for j in range(7):
                player = self.matrix[i][j]['text']
                if player != ' ' \
                        and player == self.matrix[i+1][j]['text'] \
                        and player == self.matrix[i+2][j]['text']  \
                        and player == self.matrix[i+3][j]['text']:
                    return player
        # 대각선 좌에서 우로
        for i in range(3):  # row=0,1,2
            for j in range(3, 7):  # col=3,4,5,6
                player = self.matrix[i][j]['text']
                if self.matrix[i][j]["text"] != " " \
                        and self.matrix[i][j]["text"] == self.matrix[i + 1][j - 1]["text"] \
                        and self.matrix[i][j]["text"] == self.matrix[i + 2][j - 2]["text"] \
                        and self.matrix[i][j]["text"] == self.matrix[i + 3][j - 3]["text"]:
                    return player
        # 대각선 우에서 좌로
        for i in range(3):  # row=0,1,2
            for j in range(3, 7):  # col=3,4,5,6
                player = self.matrix[i][j]['text']
                if self.matrix[i][j]["text"] != " " \
                        and self.matrix[i][j]["text"] == self.matrix[i + 1][j - 1]["text"] \
                        and self.matrix[i][j]["text"] == self.matrix[i + 2][j - 2]["text"] \
                        and self.matrix[i][j]["text"] == self.matrix[i + 3][j - 3]["text"]:
                    return player
        return ' '

    def findrow(self, col):
        for row in range(5, -1, -1):
            if self.matrix[row][col]['text'] == ' ':
                return row


MainGUI()
