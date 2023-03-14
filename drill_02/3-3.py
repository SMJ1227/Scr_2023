'''
광주, 부산, 강릉, 서울 네 도시에 의해 둘러 쌓여진 넓이의 추정 넓이를 계산하시오
'''

import math


x1, y1 = 35.1768201, 126.7735892  # 광주
x2, y2 = 35.1645701, 129.0015892  # 부산
x3, y3 = 37.7637326, 128.8824475  # 강릉
x4, y4 = 37.565289, 126.8491257   # 서울

s12 = math.sqrt(((x1 - x2)**2) + ((y1-y2)**2))
s23 = math.sqrt(((x2 - x3)**2)+((y2-y3)**2))
s31 = math.sqrt(((x3 - x1)**2)+((y3-y1)**2))
s_u = (s12+s23+s31)/2
area_u = math.sqrt(s_u*(s_u-s12)*(s_u-s23)*(s_u-s31))

s34 = math.sqrt(((x3 - x4)**2) + ((y3-y4)**2))
s41 = math.sqrt(((x4 - x1)**2)+((y4-y1)**2))
s_o = (s31+s34+s41)/2
area_o = math.sqrt(s_o*(s_o-s31)*(s_o-s34)*(s_o-s41))

print(area_u + area_o)
