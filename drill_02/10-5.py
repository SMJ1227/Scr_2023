list1 = [eval(s) for s in input('10개의 숫자를 입력하세요:').split()]
list2 = []
for i in list1:
    if not i in list2:
        list2.append(i)
print("중복을 제거한 고유한 숫자: ", list2)

print('Ref. 10-5')
list2 = [1, 21, 13]
print(list1 + list2)
print(2 * list1)
print(list2 * 2)
print(list1[1: 3])
print(list1[3])
