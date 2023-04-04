def dateToInt(date): #  "2022.05.19" 날짜를 2000.01.01을 1로 시작하는 정수로 변환
    year = int(date[0:4]) # 2000~2022
    month = int(date[5:7])
    day = int(date[8:])

    return (year-2000)*12*28 + (month-1)*28 + day

def solution(today, terms, privacies):
    answer = []
    #1단계 today "2022.05.19" 날짜를 "2000.01.01"을 1로 시작하는 정수로 변환
    todayInteger = dateToInt(today)
    #print(dateToInt('2000.01.01'))
    #print(dateToInt('2000.02.01'))
    #print(dateToInt('2001.01.01'))

    #2단계 terms ["A 6", "B 12", "C 3"] 사전으로 만듦 key:약관 / value:유효기간일수
    termsDic = dict() #비어있는 사전 생성
    for t in terms:
        termsDic[t[0]] = int(t[2:])*28 # key/value쌍을 사전에 추가
    #print(termsDic)

    #3단계 privacies["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    #현재 날짜가 개인정보 수집일 + 약관 유효기간 - 1보다 크면 파기한다.
    for i in range(len(privacies)):
        date = privacies[i][:10]  #i번째 개인정보 수집 날짜
        pickDayInteger = dateToInt(date) #i번째 개인정보 수집 날짜를 정수로 변환
        term = privacies[i][11] #i번째 개인정보약관
        if todayInteger > (pickDayInteger + termsDic[term] - 1):
            answer.append(i+1)

    return answer

# print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))

# https://school.programmers.co.kr/learn/courses/30/lessons/150370
