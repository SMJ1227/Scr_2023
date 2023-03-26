def ex14_2():
    ilist = [eval(s) for s in input('정수 리스트 입력:').split()]
    d = {}
    for n in ilist:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
        maxCount = max(d.values())
        for k, v in d.items():
            if v == maxCount:
                print(k, end=' ')
        print()
ex14_2()
