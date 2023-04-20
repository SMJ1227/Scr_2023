'''plus = 0
minus = 0
equal = 0
T = eval(input()) # 테스트 케이스 개수
symbol = input()
for i in range(T): # 테스트 케이스 개수만큼 반복
    #print(symbol[i])
    if symbol[i] == '+':
        plus += 1
    elif symbol[i] == '-':
        minus += 1
    elif symbol[i] == '=':
        equal += 1
#line = max(plus, minus)
#arr = [['.' for j in range(line)] for i in range(T)]
#now_line = plus
#for j in range(line):
#    for i in range(T):
#        print(arr[i][j], end='')
#    print()'''

'''
T = eval(input()) # 테스트 케이스 개수
symbol = input()
arr = ['.'*T]
for i in range(T): # 테스트 케이스 개수만큼 반복
    arr.insert(arr)
    print(arr)
'''
n = eval(input())
changes = input()

min_row = -1
max_row = 1
cur_row = 0
cur_col = 0

for i in range(n-1):
    if changes[i] == '+':
        if changes[i+1] == '+':
            cur_row -= 1
        else:
            pass
    elif changes[i] == '-':
        if changes[i+1] == '-':
            cur_row += 1
        else:
            pass

    min_row = min(min_row, cur_row)
    max_row = max(max_row, cur_row)

width = n
height = max_row - min_row + 1

matrix = [['.' for _ in range(width)] for _ in range(height)]

cur_row = -min_row

for c in changes:
    if c == '+':
        matrix[cur_row][cur_col] = '/'
        cur_row -= 1
    elif c == '-':
        matrix[cur_row][cur_col] = '\\'
        cur_row += 1
    else:
        matrix[cur_row][cur_col] = '_'
    cur_col += 1

for row in matrix:
    print(''.join(row))
