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

#속한 노래가 많이 재생된 장르를 먼저 수록합니다.
#장르 내에서 많이 재생된 노래를 먼저 수록합니다.
#장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
#print(plays) #재생횟수 출력
#print(max(plays)) # 재생횟수 최대값 출력
#print(D) #딕셔너리 출력
#print(plays.index(max(plays))) # 재생횟수중 재생횟수가 최대값 인덱스 출력
#print(plays[0])
#print(D[genres[0]][0])# 장르별 재생횟수
#print(sorted(D, reverse=True))
# for i in range(2):
#     for j in range(2):
#         print(D[genres[i]][0])
#print(sorted_dict)

sorted_dict = sorted(D.items(), key=lambda x: x[1], reverse=True)
for i in range(len(sorted_dict)):
    for j in range(1, 3):
        if sorted_dict[i][1][j][0] == -1:
            pass
        else:
            print(sorted_dict[i][1][j][0])
