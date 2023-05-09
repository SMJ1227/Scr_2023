import random
from tkinter import *

class MainGUI():
    def __init__(self):
        window = Tk()
        window.title('행맨 게임')
        self.canvas = Canvas(window, bg='white', width=400, height=300)
        self.canvas.pack()
        fp = open('hangman.txt')
        self.words = fp.read().split()
        self.setWord()
        self.drawHangman()
        #Canvas key 입력에 대한 이밴트 bind
        self.canvas.bind('<Key>', self.KeyEvent)
        self.canvas.focus_set()

        window.mainloop()

    def toString(self, guessWord):
        result = ''
        for ch in guessWord:
            result += ch
        return result

    def drawHangman(self):
        self.canvas.delete('hangman')
        self.canvas.create_arc(20, 200, 20+80, 200+40, start=0, extent=180)  #아크 베이스
        self.canvas.create_line(20+40, 200, 20+40, 20)                      #  폴대
        self.canvas.create_line(20+40, 20, 20+40+100, 20)                   #  행거

        if self.doneWithWrong:  # 7번 틀린경우
            self.canvas.create_text(200, 250, text='정답 ' + self.toString(self.hiddenWord),
                                    font='Times 14', tags='hangman')
            self.canvas.create_text(200, 270, text='계속하려면 ENTER', font='Times 14', tags='hangman')
        elif self.doneWithCorrect:  # 정답을 맞춘 경우
            self.canvas.create_text(200, 250, text='맞았습니다. ' + self.toString(self.guessWord),
                                    font='Times 14', tags='hangman')
            self.canvas.create_text(200, 270, text='계속하려면 ENTER', font='Times 14', tags='hangman')
        else:
            self.canvas.create_text(200, 250, text='단어 추측 ' + self.toString(self.guessWord),
                                    font='Times 14', tags='hangman')
            if self.NofMiss > 0:
                self.canvas.create_text(200, 270, text='틀린 글자 ' + self.toString(self.missChar),
                                        font='Times 14', tags='hangman')

        if self.NofMiss < 1:
            return
        x1 = 20+40+100
        y1 = 20
        x2 = x1
        y2 = y1+20
        self.canvas.create_line(x1, y1, x2, y2, tags='hangman')  # 행거
        if self.NofMiss < 2:
            return
        x3 = x2
        y3 = y2 + 20
        self.canvas.create_oval(x3-20, y3-20, x3+20, y3+20, tags='hangman')
        if self.NofMiss < 3:
            return
        self.canvas.create_line(x3-15, y3+15, x3-50, y3+70, tags='hangman')
        if self.NofMiss < 4:
            return
        self.canvas.create_line(x3+15, y3+15, x3+50, y3+70, tags='hangman')
        if self.NofMiss < 5:
            return
        x4 = x3
        y4 = y3 + 100
        self.canvas.create_line(x3, y3+20, x4, y4, tags='hangman')
        if self.NofMiss < 6:
            return
        self.canvas.create_line(x4, y4, x4-50, y4+80, tags='hangman')
        if self.NofMiss < 7:
            return
        self.canvas.create_line(x4, y4, x4+50, y4+80, tags='hangman')

    def setWord(self):
        index = random.randint(0, len(self.words) - 1)
        self.hiddenWord = self.words[index]
        self.guessWord = ['*'] * len(self.hiddenWord)
        self.NofCorrectChar = 0
        self.NofMiss = 0
        self.missChar = []
        self.doneWithWrong = False
        self.doneWithCorrect = False

    def KeyEvent(self, Key):
        if 'a' <= Key.char <= 'z':
            if Key.char in self.guessWord:
                print('\t', Key.char, '은/는 이미 포함되어 있습니다.')
            elif self.hiddenWord.find(Key.char) == -1:
                print('\t', Key.char, '은/는 포함되어 있지 않습니다.')
                self.NofMiss += 1
                if not Key.char in self.missChar:
                    self.missChar.append(Key.char)
                if self.NofMiss == 7:
                    self.doneWithWrong = True  # 7번 틀리고 못맞추고 종료

            else:
                k = self.hiddenWord.find(Key.char)
                while k >= 0:
                    self.guessWord[k] = Key.char
                    self.NofCorrectChar += 1
                    k = self.hiddenWord.find(Key.char, k + 1)
                if self.NofCorrectChar == len(self.hiddenWord):
                    self.doneWithCorrect = True  # 정답 찾고 종료
        elif Key.keycode == 13:
            if self.doneWithCorrect or self.doneWithWrong:
                self.setWord()
                self.drawHangman()
        self.drawHangman()

MainGUI()




'''
def main():
    #words = ['write', 'program', 'that', 'teacher', 'student', 'korea', 'hangman']
    fp = open('hangman.txt')
    words = fp.read().split()
    while True:
        index = random.randint(0, len(words) - 1)
        hiddenWord = words[index]
        guessWord = ['*'] * len(hiddenWord)
        NofCorrectChar = 0
        NofMiss = 0
        while NofCorrectChar < len(hiddenWord):
            ch = input('(추측) 단어' + toString(guessWord) + '에 포함되는 문자를 입력 > ')
            if ch in guessWord:
                print('\t', ch, '은/는 이미 포함되어 있습니다.')
            elif hiddenWord.find(ch) == -1:
                print('\t', ch, '은/는 포함되어 있지 않습니다.')
                NofMiss += 1
            else:
                k = hiddenWord.find(ch)
                while k >= 0:
                    guessWord[k] = ch
                    NofCorrectChar += 1
                    k = hiddenWord.find(ch, k+1)
        print('정답은 ', hiddenWord, '입니다', NofMiss, '번 실패했습니다.')
        YesNo = input('다른 단어 맞추기를 하시겠습니까? Y / N > ')
        if YesNo == 'n':
            break

def toString(guessWord):
    result = ''
    for c in guessWord:
        result += c
    return result

main()
'''
