filename = input('파일 이름을 입력:')
ifp = open(filename)
s = ifp.read()
print('문자개수:',len(s))
# sList = s.split()
print('단어개수:',len(s.split()))
#ifp.seek(0)
#lines = ifp.readlines()
print('행개수:',len(s.split('\n')))#lines))
ifp.close()
