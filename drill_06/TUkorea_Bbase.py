# b진법
# 1단계 b진수 숫자 2개를 입력받는다.
# 4 4 2
# 3 3 1 2
# 3 0

#b, M, N = map(eval, input().split())
[b, N, M] = [eval(s) for s in input().split()] # 첫번째 줄 : 숫자 3개
Nlist = [eval(s) for s in input().split()]  # 두번째 줄 : 숫자 N개
Mlist = [eval(s) for s in input().split()]  # 세번째 줄 : 숫자 M개

# 2단계 b진수 숫자 2개를 10진수로 변환
# dn-1 ... d0 (b진수) =d0 + d1 * b + d2 * b^2 + ... + di * b^i + ... + dn-1 * b^(n-1) (10진수)
N10 = 0  # [3, 3, 1, 2]
for e in Nlist:
    N10 = N10 * b + e  # (((0*4 + 3) * 4 + 3) * 4 + 1) * 4 + 2
M10 = 0
for e in Mlist:
    M10 = M10 * b + e  # (0*4 + 3) * 4 + 0

# 3단계 10진수로 변환한 두 숫자를 곱한다.
P = N10 * M10

# 4단계 10진수 결과를 b진수로 변환한다.
Pblist = []
while P: # P가 0이 아니면 반복
    Pblist.insert(0, P % b) # 항상 첫번째 자리에 b로 나눈 나머지를 삽입
    P //= b
print(len(Pblist))
for i in range(len(Pblist)):
    if i == len(Pblist)-1:
        print(Pblist[i])
    else:
        print(Pblist[i], end=' ')
