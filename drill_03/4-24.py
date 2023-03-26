import random

num = random.randrange(1, 13)
pat = random.randrange(1, 4)

if pat == 1:
    pat = "스페이드"
elif pat == 2:
    pat = "하트"
elif pat == 3:
    pat = "클로버"
elif pat == 4:
    pat = "다이아몬드"

if num == 1:
    num = "A"
if num == 11:
    num = "J"
if num == 12:
    num = "Q"
if num == 13:
    num = "K"

print('당신이 뽑은 카드는 ', pat, num, '입니다.')
