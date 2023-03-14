'''
삼각형의 세 꼭짓점 좌표를 입력하고
삼각형의 넓이를 출력하는 프로그램 작성
s = (s1+s2+s3)/2
area  = math.sqrt(s(s-s1)(s-s2)(s-s3))
'''

import math

x1, y1, x2, y2, x3, y3 = eval(input("삼각형의 세 꼭짓점을 입력하세요: "))
s1 = math.sqrt(((x1 - x2)**2) + ((y1-y2)**2))
s2 = math.sqrt(((x2 - x3)**2)+((y2-y3)**2))
s3 = math.sqrt(((x3 - x1)**2)+((y3-y1)**2))
s = (s1+s2+s3)/2
area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print(area)
