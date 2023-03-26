ilist = [eval(s) for s in input('정수 입력: ').split()]
ave = sum(ilist) / len(ilist)
upc = 0
dwc = 0
for i in ilist:
    if i >= ave:
        upc += 1
    elif i < ave:
        dwc += 1

print(upc, dwc)

print(ilist.index(1))
print(ilist.count(1))
print(len(ilist))
print(max(ilist))
print(min(ilist))
print(sum(ilist))
