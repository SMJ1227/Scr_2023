def displaySortedNumbers(num1, num2, num3):
    numlist = [num1, num2, num3]
    list.sort(numlist)
    for s in range(len(numlist)):
        print(numlist[s], end=' ')

num1, num2, num3 = eval(input())

displaySortedNumbers(num1, num2, num3)
