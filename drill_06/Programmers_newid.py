def solution(new_id):
    answer = ''

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
#    "...!@BaT#*..y.abcdefghijklm" → "...!@bat#*..y.abcdefghijklm"
    new_id = new_id.lower()

# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
#    "...!@bat#*..y.abcdefghijklm" → "...bat..y.abcdefghijklm"
    for c in new_id:
        if c.isalnum() or c =='-' or c == '_' or c== '.':
            answer += c
    new_id = answer
    answer = ''

# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
#    "...bat..y.abcdefghijklm" → ".bat.y.abcdefghijklm"
    first = True
    for c in new_id:
        if c == '.':
            if first:
                answer += c
                first = False
        else:
            answer += c
            first = True

# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]

# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if not answer: # 비어있으면
        answer = 'a'

# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(answer) > 15:
        answer = answer[:15] # 15글자로 자름
        if answer[-1] == '.':
            answer = answer[:-1]

# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(answer) <= 2:
        answer += answer[-1]

    return answer

# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))

# https://school.programmers.co.kr/learn/courses/30/lessons/72410