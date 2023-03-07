friend = 10
Friend = 1
print(type(friend))
print(type(Friend))
print(friend)
print(Friend)

a, b = 1, 2
print(type(a))
print(type(b))
print(a)
print(b)

e=f=g=1
print(type(e))
print(type(g))
print(type(f))
print(e)
print(f)
print(g)
if 1<=e<2:
    print('yee')

print(0o10)
print(0o20)
print(0x10)
print(0xf)
print(0b10)
print(oct(38)) #8진수
print(hex(38)) #16진수
print(hex(255))
print(bin(255)) #2진수

c = 1.0
d = 3.0
print(type(c))
print(type(d))

pi = 3.14
print(type(pi))
pi = 314e-2
print(type(pi))
print(pi)

x = 3-4j
print(type(x))
print(x.real)
print(x.imag)
print(x.conjugate())

r = 10
circle_area = pi * (r ** 2) # 원의 넓이
print(circle_area)
x = 3
y = 4
triangle_area = x* y / 2 # 삼각형의 넓이
print(triangle_area)

print(2/3) # 실수 나눗셈
print(5/2)
print(2//3) # 정수 나눗셈
print(5//2)

'kim'
print(type('kim'))
print(type("kim"))
print('''
영원에 살고 순간에 살아라
...
-리히텐베르크
''')

#프로그램설명
#함수1
#더하기 함수
'''
프로그램설명
함수1
더하기 함수
''' # 주석 처리

print('\t탭\n다음줄')
print(r'\t탭\n다음줄')

print('py' + 'thon')
print('py' * 3)
a = 'python'
print(a[0])
print(a[1])
print(a[0:2])
#print(a[6])
print(a[-1])
print(a[-3:]) # 끝까지
print(a[:3]) # 처음부터
print(a[::2]) # 두칸씩
print(a[::-1]) # 역순

print(str(3.14))
print(int('49'))
print(float('4.5'))
print(eval('1'))
print(eval('3.14'))


