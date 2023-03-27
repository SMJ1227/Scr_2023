count = 1

def main():
    n = eval(input('디스크의 개수를 입력하세요: '))
    # 해결 방법을 재귀적으로 찾는다.
    print('옮기는 순서는 다음과 같습니다:')
    moveDisks(n, 'A', 'B', 'C')
    # auxTower를 사용하여 fromTower에서 toTower까지
    # n개의 디스크를 옮기는 해결방법을 찾는 함수

def moveDisks(n, fromTower, toTower, auxTower):
    global count

    if n == 1:  # 정지 조건
        print(count, '디스크 ', n, '을/를 ', fromTower, '에서 ', toTower, '로 옮긴다.')
        count += 1
    else:
        moveDisks(n-1, fromTower, auxTower, toTower)
        print(count, '디스크 ', n, '을/를 ', fromTower, '에서 ', toTower, '로 옮긴다.')
        count += 1
        moveDisks(n-1, auxTower, toTower, fromTower)


main()
