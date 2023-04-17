T = eval(input()) # 테스트 케이스 개수
for _ in range(T): # 테스트 케이스 개수만큼 반복
    [num1, math, num2, equal, ans] = input().split()
    N1 = int(num1)
    N2 = int(num2)
    answer = int(ans)
    if math == '+':
        judge = N1 + N2
    elif math == '-':
        judge = N1 - N2
    elif math == '*':
        judge = N1 * N2
    elif math == '/':
        judge = N1 // N2
    if (judge == answer):
        print('correct')
    else:
        print('wrong answer')

