# 다음 N개의 줄에 각 회사별 주식을 구매했을 때,
# 그날 그날의 손익을 나타내는 3개의 정수 A, B, C (-1,000,000 ≤ A, B, C ≤1,000,000)가 주어진다. 500 800 200
# A는 A사의 주식을 구매했을 때의 손익, B는 B사의 주식을 구매했을 때의 손익, C는 C사의 주식을 구매했을 때의 손익을 나타낸다.

T = eval(input()) # 테스트 케이스 개수

for i in range(T): # 테스트 케이스 개수만큼 반복
    money = 0
    N = eval(input())
    for j in range(N):
        array = [eval(s) for s in input().split()]
        if max(array) < 0:
            pass
        else:
            money += max(array)
    print(money)
