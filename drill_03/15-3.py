'''(재귀를 이용하여 최대공약수 계산하기) 은 다음과 같이 재귀적으로 정
의될 수도 있다.
 𝑚 % 𝑛 이 0이면, gcd(𝑚, 𝑛)은 𝑛𝑛이다.
 그렇지 않으면, gcd(𝑚, 𝑛) 은 gcd(𝑛, 𝑚 % 𝑛)이다.
 최대공약수(GCD)를 구하는 재귀 함수를 작성하시오. 또한 사용자로부터 두 정
수를 입력 받고 두 정수의 GCD를 출력하는 예제 프로그램을 작성하시오.
'''

def gcd(m, n):
    if m % n == 0:
        return n
    return gcd(n, m % n)

m, n = eval(input())
print('최대공약수:', gcd(m, n))