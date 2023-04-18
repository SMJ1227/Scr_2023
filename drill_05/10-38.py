from tkinter import *
import random
import tkinter.messagebox

width = 600
height = 400
barwidth = (width - 20) / 20 # 막대 하나의 넓이

class MainGUI:
    def __init__(self):
        window = Tk()
        window.title("선택정렬 애니메이션")
        self.canvas = Canvas(width=width, height=height, bg='white')
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        Button(frame, text='다음단계', command=self.step).pack(side=LEFT)
        Button(frame, text='재시작', command=self.reset).pack(side=LEFT)
        for i in range(20):
            self.l = [i for i in range(1, 21)]
        window.mainloop()

    def step(self):
        self.cur += 1
        minvalue = min(self.l[self.cur:])
        minindex = self.l.index(minvalue)
        self.l[self.cur], self.l[minindex] = self.l[minindex], self.l[self.cur]
        self.draw()

    def reset(self):
        random.shuffle(self.l)
        self.cur = -1 # 막대그래프의 위치 변수
        self.draw()

    def draw(self):
        self.canvas.delete('line')
        for i in range(20):
            x0 = 10 + i*barwidth
            x1 = 10 + (i+1)*barwidth
            y0 = height - (height-20)*self.l[i]/20
            y1 = height - 10
            if i == self.cur:
                self.canvas.create_rectangle(x0, y0, x1, y1,fill='red', tags='line')
            else:
                self.canvas.create_rectangle(x0, y0, x1, y1, tags='line')
                self.canvas.create_text(x0+(barwidth/2), y0+5, text=str(self.l[i]), tags='line')

MainGUI()
