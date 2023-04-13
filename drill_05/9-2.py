from tkinter import *

class MainGUI:
    def __init__(self):
        window = Tk()
        window.title('투자금 계산기')
        Label(window, text='투자금').grid(row=0, column=0, sticky=W)
        Label(window, text='기간(월)').grid(row=1, column=0, sticky=W)
        Label(window, text='연이율(%)').grid(row=2, column=0, sticky=W)
        Label(window, text='미래가치').grid(row=3, column=0, sticky=W)

        self.e1 = Entry(window, justify=RIGHT)
        self.e1.grid(row=0, column=1)
        self.e2 = Entry(window, justify=RIGHT)
        self.e2.grid(row=1, column=1)
        self.e3 = Entry(window, justify=RIGHT)
        self.e3.grid(row=2, column=1)

        self.label = Label(window, text='')
        self.label.grid(row=3, column=1, sticky=E)

        Button(window, text='계산하기', command=self.compute).grid(row=6, column=1, sticky=E)

        window.mainloop()

    def compute(self):
        money = eval(self.e1.get())
        month = eval(self.e2.get()) * 12
        month_rate = eval(self.e3.get()) / 1200
        future_value = money * ((1 + month_rate) ** month)
        self.label['text'] = '{0:.2f}'.format(future_value)
        pass

MainGUI()
