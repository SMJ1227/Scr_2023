name = input('사원 이름을 입력하세요: ')
hour = eval(input('주 당 근무시간을 입려하세요: '))
pay = eval(input('시간 당 급여를 입력하세요: '))
tax = eval(input('원천징수세율을 입력하세요: '))
tax2 = eval(input('지방세율을 입력하세요: '))

print('사원 이름:', name)
print('주당 근무시간:', hour)
print('임금:', pay)
print('총 급여:', hour*pay)
print('공제',
      '원천징수세(%.2f): ' % tax, '%.2f' % (hour*pay*tax),
      '주민세(%.2f): ' % tax2, '%.2f' % (hour*pay*tax2),
      '총 공제: ', (hour*pay*tax)+(hour*pay*tax2),
      '공제 후 급여: ', (hour*pay) - ((hour*pay*tax)+(hour*pay*tax2))
)


