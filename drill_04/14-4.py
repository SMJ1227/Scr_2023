from tkinter import *
from tkinter.filedialog import askopenfilename

def openFile():
    f = askopenfilename() # 파일 오픈 탐색기에서 파일 선택 후 이름을 반환
    filename.set(f)

def showResult():
    fp = open(filename.get()) # 파일오픈
    histogram = [0]*26 # a~z 빈도수를 세는 리스트
    s = fp.read().lower() # 파일을 내용을 문자열로 읽고 소문자로 변환 후 s로 전달
    for c in s: # 문자열 s에서 문자 하나씩 c로 가져와서 빈도수 세기
        if c.isalpha():
            histogram[ord(c) - ord('a')] += 1
    for i in range(26): # 빈도수를 text 상자에 쓰기
        if histogram[i]:
            text.insert(END, chr(i+ord('a'))+' - '+str(histogram[i])+'번 나타납니다.\n')

window = Tk()
window.title('문자의 빈도수 세기')

frame1 = Frame(window)
frame1.pack()
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(frame1, width=40, height=10, wrap=WORD, yscrollcommand=scrollbar.set)
text.pack()
scrollbar.configure(command=text.yview)

frame2 = Frame(window)
frame2.pack()
Label(frame2, text='파일 이름 입력:').pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable=filename).pack(side=LEFT)
Button(frame2, text='열기', command=openFile).pack(side=LEFT)
Button(frame2, text='결과보기', command=showResult).pack(side=LEFT)

window.mainloop()