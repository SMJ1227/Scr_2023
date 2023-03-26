import random

n = eval(input('공의 개수: '))
s = eval(input('슬롯의 개수:'))
slots = [0]*s

for i in range(n):
    count = 0
    for i in range(s-1):
        if(random.random() > 0.5):
           print('R',end='')
           count += 1
        else:
            print('L',end='')
    slots[count] += 1
    print()
print(slots)

v = max(slots)
for h in range(v, 0, -1):
    for i in range(s):
        if slots[i] >= h:
            print('@',end='')
        else:
            print('.',end='')
    print()
