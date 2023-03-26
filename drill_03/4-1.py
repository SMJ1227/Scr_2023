a, b, c = eval(input("a,b,c 입력: "))
D = (b**2)-(4*a*c)

if D < 0:
    print("이 방정식은 실근이 존재하지 않습니다.")
elif D == 0:
    r1 = -b / (2*a)
    print('실근은 %d입니다.' % r1)
elif D > 0:
    r1 = (-b+D**0.5)/(2*a)
    r2 = (-b-D**0.5)/(2*a)
    print('실근은 %f과' % r1, ' %f입니다.' % r2)
