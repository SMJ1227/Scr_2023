def ex10_15():
    ilist = [eval(s) for s in input('리스트를 입력하세요: ').split()]
    if isSorted(ilist) is True:
        print('리스트는 이미 정렬되어 있습니다.')
    else:
        print('리스트는 정렬되어 있지 않습니다.')

def isSorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

ex10_15()
