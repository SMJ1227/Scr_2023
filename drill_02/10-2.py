# s = input('정수 리스트 입력: ')
# slist = s.split()
# ilist = [eval(s) for s in slist]
ilist = [eval(s) for s in input('정수 리스트 입력:').split()]
# ilist = list(map(eval, input('정수 리스트 입력:').split()))
ilist.reverse()

for i in ilist:
    print(i, end=' ')

print()
print('Ref. 10-2')
print('lst에 몇 개의 원소가 있는가?', len(ilist))
print('lst의 첫 번째 원소의 인덱스는?', ilist[0])
print('lst의 마지막 원소의 인덱스는?', ilist[len(ilist)-1])
print('lst[2]의 값은?', ilist[2])
print('lst[-2]의 값은?', ilist[-2])
