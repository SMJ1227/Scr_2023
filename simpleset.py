from functools import*

def intersect(*ar):
    return reduce(__intersectSC, ar)

def __intersectSC(listX, listY):
    setList = []
    for x in listX:
        if x in listY:
            setList.append(x)
    return setList

def difference(*ar):
    setList = []
    intersectSet = intersect(*ar)
    unionSet = union(*ar)
    for x in unionSet:
        if not x in intersectSet:
            setList.append(x)
    return setList

def union(*ar):
    setList = []
    for item in ar:
        for x in item:
            if not x in setList:
                setList.append(x)
    return setList

if __name__ == '__main__':
    A = [1,2,3]
    B = [2,3,4]
    C = [3,4,5]

    print(intersect(A,B,C))
