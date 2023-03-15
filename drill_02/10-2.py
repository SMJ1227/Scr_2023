# s = input('정수 리스트 입력: ')
# slist = s.split()
# ilist = [eval(s) for s in slist]
# ilist = [eval(s) for s in input('정수 리스트 입력:').split()]
ilist = list(map(eval, input('정수 리스트 입력:').split()))
ilist.reverse()

for i in ilist:
    print(i, end=' ')
