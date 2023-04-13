from tkinter import *
import random

width = 600
height = 400

class MainGUI:
    def __init__(self):
        window = Tk()
        window.title('공튀기기')
        self.balllist = [] # 볼 객체 리스트
        self.isstop = False # 정지 재시작 제어 변수
        self.sleep = 100 # 밀리초 단위, 빠르기 제어 변수
        self.canvas = Canvas(window, width=width, height=height, bg='white')
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        Button(frame, text='정지', command=self.stop).pack(side=LEFT)
        Button(frame, text='재시작', command=self.resume).pack(side=LEFT)
        Button(frame, text='+', command=self.add).pack(side=LEFT)
        Button(frame, text='-', command=self.remove).pack(side=LEFT)
        Button(frame, text='빠르게', command=self.faster).pack(side=LEFT)
        Button(frame, text='느리게', command=self.slower).pack(side=LEFT)
        self.animate()
        window.mainloop()

    def stop(self):
        self.isstop = True

    def resume(self):
        self.isstop = False
        self.animate()

    def add(self):
        self.balllist.append(Ball()) # Ball 객체 생성해서 리스트에 추가

    def remove(self):
        if self.balllist:
            self.balllist.pop()

    def faster(self):
        if self.sleep > 20:
            self.sleep -= 20

    def slower(self):
        self.sleep += 20

    def animate(self):
        while not self.isstop:
            self.canvas.after(self.sleep) # sleep밀리초동안 쉬었다가
            self.canvas.update()
            self.canvas.delete('ball')
            for ball in self.balllist: # balllist에 있는 모든 Ball객체를 다시 그린다
                if ball.x >= width: # 우측으로 넘어가면
                    ball.dx = -2
                elif ball.x < 0:
                    ball.dx = 2
                elif ball.y >= height: # 하단 넘어가면
                    ball.dy = -2
                elif ball.y < 0:
                    ball.dy = 2
                ball.x += ball.dx
                ball.y += ball.dy
                self.canvas.create_oval(ball.x-5, ball.y-5, ball.x+5, ball.y+5, fill=ball.color, tags='ball')

class Ball:
    def __init__(self):
        colors = ['red', 'orange', 'blue', 'white', 'black', 'yellow', 'cyan']
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.dx = 2 # x방향
        self.dy = 2 # y뱡향
        self.color = random.choice(colors)

MainGUI()
