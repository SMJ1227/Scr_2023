def ex10_8():
    ilist = [eval(s) for s in input('정수 리스트 입력:').split()]
    print('가장 작은 정수의 인덱스: ',indexOfSmallestElement(ilist))

def indexOfSmallestElement(lst):
    min = lst[0]
    index = 0
    for i in range(1, len(lst)):
        if min > lst[i]:
            min = lst[i]
            index = i
    return index
ex10_8()
