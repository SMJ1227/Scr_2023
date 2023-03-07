#reverse함수 = 1234입력시 4321반환
def reverse(N):
    result = 0
    # result = result * 10 + N % 10; N//10
    # result = (result * 10 + N % 10) * 10 + N % 10; N//10
    # result = ((result * 10 + N % 10) * 10 + N % 10) * 10 + N % 10; N//10
    # result = (((result * 10 + N % 10) * 10 + N % 10) * 10 + N % 10) * 10 + N % 10; N//10; N//10
    while N: #N이 0이 아닐때 까지
        result = result * 10 + N % 10
        N = N//10
    return result

#소수 판정 함수
def isPrime(N):
    #N을 2,3,4,5,...,int(N**0.5)까지 나눠서 떨어지지 않아야 한다
    for divisor in range(2, int((N**0.5)+1)):
        if N % divisor == 0:
            return False
    return True

# 1. 표준 입력으로 n을 읽는다
N = eval(input())

# 2. palindrome 검사
# N과 reverse(N)이 같은지 검사.

while True:
    if N == reverse(N) and isPrime(N): #회문 검사가 빠르므로 먼저 검사한다
        print(N)
        break
    N += 1
#print(reverse(N)) # 디버깅용
