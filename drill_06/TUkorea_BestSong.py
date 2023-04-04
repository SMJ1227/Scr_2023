# 1던계 입력받기
# 5
# classic 500
# pop 600
# classic 150
# classic 800
# pop 2500

N = eval(input()) # 곡의 갯수
genres = []
plays = []
for i in range(N):
    line = input().split()
    genres.append(line[0])
    plays.append(eval(line[1]))

# 2단계 사전 구축(key, value) key = genre, value= [총재생횟수, (1등 고유번호, 횟수), (2등 고유번호, 횟수)]
D = dict()
for i in range(N):
    if genres[i] not in D:
        D[genres[i]] = [plays[i], (i, plays[i]), (-1, 0)] # 첫 곡 정보
    else:
        D[genres[i]][0] += plays[i]
        if D[genres[i]][1][1] < plays[i]:
            D[genres[i]][2] = D[genres[i]][1]
            D[genres[i]][1] = (i, plays[i])
        elif D[genres[i]][2][1] < plays[i]:
            D[genres[i]][2] = (i, plays[i])

#print(D)
#for i in range(2):
    #print(plays)
    #print(max(plays))
print(D)
#print(plays.index(max(plays)))
