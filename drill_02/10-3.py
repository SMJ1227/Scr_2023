ilist = [eval(s) for s in input('정수 리스트 입력:').split()]
h = [0]*101 # [0, 0, ... , 0] 101개의 0을 갖는 리스트
for i in ilist:
    h[i] += 1
for i in range(1, 101):
    if h[i]:
        print(i, '-', h[i], '번 나타납니다.')
