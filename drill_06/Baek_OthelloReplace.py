# 배치된 말 중 임의의 2개의 말을 골라 서로의 위치를 바꾼다.
# 말 1개를 들어 뒤집어 놓아 색상을 변경한다.

# 1단계 입력
# 3
# 5
# WBBWW
# WBWBW

T = eval(input()) # 테스트 케이스 개수
for _ in range(T): # 테스트 케이스 개수만큼 반복
    N = eval(input()) # N = 말의 개수
    orig = input()
    goal = input() # 최소 횟수 = 최대 교환 횟수 + 나머지 뒤집기 횟수
    numberofWB = 0
    numberofBW = 0
    for i in range(N):
        if orig[i] == 'W' and goal[i] == 'B':
            numberofWB += 1
        elif orig[i] == 'B' and goal[i] == 'W':
            numberofBW += 1
    print(max(numberofWB, numberofBW))
