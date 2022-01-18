d = int(input())
if d%4 == 0 and d%100 != 0:
    print('1')
elif d%400 == 0:
    print('1')
else:
    print('0')
