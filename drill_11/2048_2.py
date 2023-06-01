from tkinter import *
from tkinter import messagebox
import random

class Game2048:
# 숫자 배경 색 사전
    bg_color = {
        2: '#eee4da', 4: '#ede0c8', 8: '#edc850',
        16: '#edc53f', 32: '#f67c5f', 64: '#f65e3b',
        128: '#edcf72', 256: '#edcc61', 512: '#f2b179',
        1024: '#f59563', 2048: '#edc22e', }
    # 숫자 색 사전
    color = {
        2: '#776e65', 4: '#f9f6f2', 8: '#f9f6f2',
        16: '#f9f6f2', 32: '#f9f6f2', 64: '#f9f6f2',
        128: '#f9f6f2', 256: '#f9f6f2', 512: '#776e65',
        1024: '#f9f6f2', 2048: '#f9f6f2', }

    # nxn self.gridcell 숫자 격자에서 빈셀들만 골라서
    # cells 리스트에 그 빈셀드ㄹ의 위치 (r,c)를 넣고 그 중에서 랜덤하게 골라서 2로 변경
    def random_cell(self):
        cells = []
        for r in range(self.n):
            for c in range(self.n):
                if self.gridCell[r][c] == 0: # 빈 셀이면
                    cells.append((r, c))
        curr = random.choice(cells)
        (r, c) = curr
        self.gridCell[r][c] = 2

    #nxn self.board 격자 라벨 배경 색과 숫자색 칠하기
    def paintGrid(self):
        for r in range(self.n):
            for c in range(self.n):
                if self.gridCell[r][c] == 0: # 빈 셀이면
                    self.board[r][c].configure(text='', bg='azure4') # 라벨 술자색은 없고 배경색만 칠한다.
                else:
                    self.board[r][c].configure(text=str(self.gridCell[r][c]),
                                               bg=self.bg_color[self.gridCell[r][c]],
                                               fg=self.color[self.gridCell[r][c]])

    def compressGrid(self):
        self.compress = False # 변수 초기화
        temp = [[0] * self.n for _ in range(self.n)] # nxn 0으로 초기화된 2d리스트
        for r in range(self.n):
            cnt = 0 # 제일 좌측 셀 인덱스 설정
            for c in range(self.n):
                if self.gridCell[r][c] != 0: # 빈셀이 아니면 왼쪽으로 밀착해서 temp에 넣는다
                    temp[r][cnt] = self.gridCell[r][c]
                    if cnt != c: # 실제로 빈셀로 이동한 경우
                        self.compress = True
                    cnt += 1
        self.gridCell = temp

    def mergeGrid(self): #좌우 인접 셀이 같으면 숫자를 2배로 merge
        self.merge = False
        for r in range(self.n):
            for c in range(self.n - 1):
                if self.gridCell[r][c] == self.gridCell[r][c + 1] and self.gridCell[r][c] != 0:
                    self.gridCell[r][c] *= 2
                    self.gridCell[r][c + 1] = 0
                    self.score += self.gridCell[r][c]
                    self.merge = True

    def reverse(self): # nxn self.gridCell 숫자 격자의 모든 행을 reverse
        for r in range(self.n):
            self.gridCell[r].reverse()

    def transpose(self):
        self.gridCell = [list(t) for t in zip(*self.gridCell)]

    def can_merge(self): # 상하좌우 merge할 셀이 있는가
        # 좌우로 인접셀 검사
        for r in range(self.n):
            for c in range(self.n-1):
                if self.gridCell[r][c] == self.gridCell[r][c+1]:
                    return True
        #상하로 인접셀 검사
        for r in range(self.n-1):
            for c in range(self.n):
                if self.gridCell[r][c] == self.gridCell[r+1][c]:
                    return True
        return False

    def link_keys(self, event):
        if self.end or self.won:
            return
        self.compress = False
        self.merge = False
        self.moved = False
        key = event.keysym
        if key == 'Up':
            self.transpose()    # 행과 열 전치
            self.compressGrid() # 밀착
            self.mergeGrid()    # 좌우 인접 셀이 같으면 merge
            self.moved = self.compress or self.merge
            self.compressGrid() #밀착
            self.transpose()    # 행과 열 전치
        elif key == 'Down':
            self.transpose()    # 행과 열 전치
            self.reverse()
            self.compressGrid() # 밀착
            self.mergeGrid()    # 좌우 인접 셀이 같으면 merge
            self.moved = self.compress or self.merge
            self.compressGrid() #밀착
            self.reverse()
            self.transpose()    # 행과 열 전치
        elif key == 'Left':
            self.compressGrid() # 밀착
            self.mergeGrid()    # 좌우 인접 셀이 같으면 merge
            self.moved = self.compress or self.merge
            self.compressGrid() #밀착
        elif key == 'Right':
            self.reverse()      # 모든 행 reverse
            self.compressGrid() # 밀착
            self.mergeGrid()    # 좌우 인접 셀이 같으면 merge
            self.moved = self.compress or self.merge
            self.compressGrid() #밀착
            self.reverse()      # 모든 행 reverse
        else:
            pass

        flag = 0
        for r in range(self.n):
            for c in range(self.n):
                if self.gridCell[r][c] == 2048:
                    flag = 1
                    break
        if flag == 1:
            self.won = True
            messagebox.showinfo('2048', 'You won')
            return
        # 2048 승리하지 않고 빈셀이 있다면 flag = 1
        for r in range(self.n):
            for c in range(self.n):
                if self.gridCell[r][c] == 0:
                    flag = 1
                    break
        if not (flag or self.can_merge()):
            self.end = True
            messagebox.showinfo('2048', 'Game over')
        if self.moved:
            self.random_cell()
        self.paintGrid()

    def __init__(self, size):
        self.n = size
        self.window = Tk()
        self.window.title('2048 Game')
        self.gameArea = Frame(self.window,  bg='azure3')
        self.gridCell = [[0]*self.n for _ in range(self.n)]
        self.compress = False
        self.merge = False
        self.moved = False
        self.end = False
        self.won = False
        self.score = 0
        self.board = []
        for r in range(self.n):
            rows = []
            for c in range(self.n):
                l = Label(self.gameArea, text='', bg='azure4', font=('arial', 22, 'bold'), width=4, height=2)
                l.grid(row=r, column=c, padx=7, pady=7)
                rows.append(l)
            self.board.append(rows)
        self.gameArea.pack()
        self.random_cell()
        self.paintGrid() # self.board 2D격자 라벨 다시 색칠
        self.window.bind('<Key>', self.link_keys) # 키 입력 이벤트 처리함수 self.link_keys 연결

        self.window.mainloop()

Game2048(4)
