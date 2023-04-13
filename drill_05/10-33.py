from tkinter import *
import random

width = 600
height = 400

class MainGUI:
    def __init__(self):
        window = Tk()
        window.title('문자 빈도수 히스토그램')
        self.canvas = Canvas(window, bg='white', width=width, height=height)
        self.canvas.pack()

        Button(window, text='히스토그램 출력', command=self.display).pack()
        window.mainloop()

    def display(self): # 천개의 소문자를 랜덤 생성해서 빈도수를 계산
        histogram = [0 for _ in range(26)]
        for _ in range(1000):
            histogram[random.randint(0, 25)] += 1

        self.canvas.delete('histogram') # 기존 막대그래프를 지우고 히스토그램을 다시 그린다
        self.canvas.create_line(10, height-10, width-10, height-10, tags='histogram')
        BarWidth = (width-20) / 26
        MaxCount = max(histogram) # 최대 빈도수를 이용해서 막대그래프의 크기를 결정한다
        for i in range(26):
            self.canvas.create_text(10+(i*BarWidth) + (BarWidth/2), height-5, text=chr(i + ord('a')), tags='histogram')
            self.canvas.create_rectangle(10+i*BarWidth, height - histogram[i]/MaxCount * (height-10), 10+(i+1)*BarWidth, height-10, tags='histogram')
            self.canvas.create_text(20+(i*BarWidth), height - histogram[i]/MaxCount * (height), text=str(histogram[i]), tags='histogram')
MainGUI()
