'''
(금융 애플리케이션: 약정 금액)
3년 후에 500만원의 적금을 받기 위해서는 매달 어느 정도의 납입금을 통장에 예금해야 하는가?
월 납입금은 다음 수식에 의해 얻을 수 있다.
월 납입금 = 약정 금액 / (1 + 월 이율) * 약정개월수
약정 금액, 연이율(%), 약정 기간(년)을 입력 받고 월 납입금을 화면에 출력하는 프로그램을 작성하시오.
'''

money = eval(input("약정 금액을 입력하세요: "))
year_rate = eval(input("연이율(%)을 입력하세요: "))
month_rate = year_rate / 1200
year = eval(input("약정 기간(년) 을 입력하세요:"))
pay = money / (1 + month_rate) ** (year * 12)
print('월 납입금은 %f입니다' % pay)
