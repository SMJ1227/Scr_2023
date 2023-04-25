n = eval(input()) # 공의 개수
s = eval(input()) # 슬롯의 개수
slots = [0] * s

for i in range(n):
    count = 0
    RL = input()
    for k in range(len(RL)):
        if RL[k] == 'R':
            count += 1
        elif RL[k] == 'L':
            pass
    slots[count] += 1

v = max(slots)
for h in range(v, 0, -1):
    for i in range(s):
        if slots[i] >= h:
            print('*', end='')
        else:
            print('.', end='')
    print()
