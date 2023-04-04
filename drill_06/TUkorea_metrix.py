def printM(M):
    for r in range(len(M)): # 행의 갯수만큼 반복
        for c in range(len(M[0])): # 열의 갯수만큼 반복
            if c == len(M[0]) - 1: # 마지막 숫자면,
                print(M[r][c]) # 숫자를 출력하고 공란없이 한 줄 띈다
            else:
                print(M[r][c],end=' ') # 숫자를 출력하고 공란 한 칸 띈다


a, b = map(eval,input().split())

M = [] # 빈 리스트, a행b열 2차워 리스트로 만들 예정.
n = 1

for r in range(a):
    temp = []
    for c in range(b):
        temp.append(n)
        n += 1
    M.append(temp)

# print(M)
print('M')
printM(M)

print('R')
R = [[M[r][c] for r in range(a-1, -1, -1)] for c in range(b)] # B행 A열 2차원 리스트
printM(R)

print('L')
L = [[M[r][c] for r in range(a)] for c in range(b-1, -1, -1)]
printM(L)

print('T')
T = [[M[r][c] for r in range(a)] for c in range(b)]
printM(T)

# 3 5 입력