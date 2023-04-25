#N, M = map(eval, input().split())
[N, M] = [eval(s) for s in input().split()]

board = [0] * N
cycle = [0] * M
for i in range(N):
    board[i] = input()
for j in range(M):
    cycle[j] = eval(input())
now = 0
count = 1
for k in range(M):
    if board[now] == '+':
        if now + cycle[k] <= N:
            now = now + cycle[k]
        else:
            pass
    elif board[now] == '-':
        if now - cycle[k] >= 0:
            now = now - cycle[k]
        else:
            pass
    if now == 0:
        count += 1
print(count)
