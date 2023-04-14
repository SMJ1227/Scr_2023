T = eval(input()) # 테스트 케이스 개수
for _ in range(T): # 테스트 케이스 개수만큼 반복
    floor_now = 0
    number_now = 1
    [floor, number, N] = [eval(s) for s in input().split()]
    for i in range(N):
        if floor_now == floor:
            floor_now = 1
            number_now += 1
        else:
            floor_now += 1
    print('{0:d}{1:02d}'.format(floor_now, number_now))
