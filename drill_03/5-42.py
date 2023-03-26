import random

num = 0
area1 = 0
area2 = 0
area3 = 0
area4 = 0
line = 0

while num < 1000000:
    num += 1
    x = random.randrange(-100, 100)
    y = random.randrange(-100, 100)
    if x < 0:
        area1 += 1
    else:
        if x == 0:
            line += 1
        elif x > 0 and y == 0:
            line += 1
        else:
            if x > 0 > y:
                area4 += 1
            elif x > 0 and y > 0:
                y1 = -x * -1 + y
                if y1 < 100:
                    area3 += 1
                elif y1 > 100:
                    area2 += 1
                elif y1 == 100:
                    line += 1

print("area1:{0}, area2:{1}, area3:{2}, area4:{3}, line:{4}".format(area1, area2, area3, area4, line))
