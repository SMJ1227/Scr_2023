x, y = eval(input("x,y 입력: "))

if x > 200 or x < 0 or y > 100 or y < 0:
    print("삼각형 외부")
else:
    y1 = -x * -0.5 + y
    if y1 <= 100:
        print("삼각형 내부")
    else:
        print("삼각형 외부")
