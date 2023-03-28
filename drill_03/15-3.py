def gcd(m, n):
    if m % n == 0:
        return n
    return gcd(n, m % n)

m, n = eval(input())
print('최대공약수:', gcd(m, n))
