from tkinter import *

width = 600
height = 200

class MainGUI:
    def __init__(self):
        window = Tk()
        window.title('라디오 버튼과 체크 버튼')
        self.canvas = Canvas(window, bg='white', width=width, height=height)
        self.canvas.pack()
        self.canvas.create_rectangle(10, 10, width-10, height-10, tag='shape')

        frame = Frame(window)
        frame.pack()
        self.v = IntVar()
        Radiobutton(frame, text='직사각형', variable=self.v, value=1, command=self.display).pack(side=LEFT)
        Radiobutton(frame, text='타원', variable=self.v, value=2, command=self.display).pack(side=LEFT)
        self.filled = IntVar() # 체크버튼 선택을 제어하는 변수
        Checkbutton(frame, text='채우기', variable=self.filled, command=self.display).pack(side=LEFT)
        window.mainloop()

    def display(self):
        self.canvas.delete('shape')
        if self.filled.get() == 1: # 채우기
            if self.v.get() == 1: # 직사각형
                self.canvas.create_rectangle(10, 10, width - 10, height - 10, fill='red', tag='shape')
            else: # 타원
                self.canvas.create_oval(10, 10, width - 10, height - 10, fill='red', tag='shape')
        else:
            if self.v.get() == 1: # 직사각형
                self.canvas.create_rectangle(10, 10, width - 10, height - 10, tag='shape')
            else: # 타원
                self.canvas.create_oval(10, 10, width - 10, height - 10, tag='shape')

MainGUI()
