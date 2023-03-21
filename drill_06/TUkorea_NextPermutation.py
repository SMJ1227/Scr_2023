#import itertools
#print(list(itertools.permutations([1, 2, 3, 4, 5], 5)))

#if list[i-1] < list[i]: 뒤에서부터 쌍으로 2개씩 비교해서 오른쪽이 크면

# 1단계 N개의 숫자로 이루어진 K개의 테스트케이스 숫자 리스트 입력
# 3 2
# 3 1 2
# 2 3 1

N, K = [eval(s) for s in input().split()]

# 2단계 K번 숫자 리스트를 입력받고 다음 순열 리스트를 출력한다.
for _ in range(K):
    L = [eval(s) for s in input().split()]
    # 3단계 뒤에서부터 쌍으로 2개씩 비교해서 오른쪽이 크면
    for i in range(N-1, 0, -1):
        if L[i-1] < L[i]:
            R = L[i-1:] # i-1번째 숫자부터 끝까지 slicing해서 R에 강제 복사
            R.sort()
            j = R.index(L[i-1])
            v = R.pop(j+1) # R [ㅓ+1]을 추출
            R.insert(0, v) # 추출한 v를 제일 앞에 삽입
            L = L[:i-1] + R
            break
    for v in L:
        print(v, end=' ')
    print()
