'''
(x1, y1)괴 (x2,y2)를 두 점의 지리학적인 위도와 경도라고 하자.
두 점 사이의 대권 거리는 다음 공식을 사용하여 계산할 수 있다.
d = r * arccos(sin(x1)*sin(x2) + cos(x1)*cos(x2)*cos(y1-y2))
사용자로부터 지구에서 두 점에 대 한 위도와 경도를 60분법 단위로 입력하게 하고
두 점의 대권 거리를 출력하는 프로그램을 작성하시오.
지구의 평균 반지름은 637001km
'''

import math

x1, y1 = eval(input("첫 번재 점(위도와 경도)을 60분법 각으로 입력하세요: "))
x2, y2 = eval(input("두 번째 점(위도와 경도)을 60분법 각으로 입력하세요: "))


r = 6370.01
d = r * math.acos(((math.sin(math.radians(x1))) * math.sin(math.radians(x2))) +
                  (math.cos(math.radians(x1))) * math.cos(math.radians(x2)) *
                  math.cos(math.radians(y1) - math.radians(y2)))

print("두 점 사이의 거리는 %f입니다." % d)
