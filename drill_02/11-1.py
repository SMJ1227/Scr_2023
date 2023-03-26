def ex11_1():
    arr = []
    for i in range(3):
        ilist = [eval(s) for s in input('정수 리스트 입력:').split()]
        arr.append(ilist)
    for j in range(4):
        print('열 %d' % j, '번 원소의 총합은 %d' % sumColumn(arr, j))

def sumColumn(m, columnIndex):
    sum = 0
    for i in range(len(m)):
        sum += m[i][columnIndex]
    return sum

ex11_1()
