'''
(금융 애플리케이션: 팁 계산하기)
소계와 팁 비율을 읽고 팁 금액과 총액을 계산하는 프로그램을 작성하시오.
예를 들면, 소계로 10과 팁 비율로 15%를 입력하면,
팁 금액으로 1.5와 총액으로 11.5를 출력한다.
'''

pay, rate = eval(input("소계와 팁 비율을 입력하세요: "))
tip = pay / 100 * rate
total = pay + tip
print('팁은 %.2f이고' % tip, ' 총액은 %.2f입니다.' % total)
