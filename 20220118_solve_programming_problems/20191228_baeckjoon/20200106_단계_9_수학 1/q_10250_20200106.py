# File encoding: UTF-8
# 1
import sys

t = int(sys.stdin.readline())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())

    if n <= h:
        x = 1
        y = n
    else:
        if n % h == 0:  # 나머지
            x = n//h  # 몫
            y = h
        else:
            x = n//h + 1
            y = n % h

    if x < 10:
        print(str(y)+'0'+str(x))
    else:
        print(str(y)+str(x))


# 2
import sys

t = int(sys.stdin.readline())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())

    x = 1
    y = 0
    while 0 < n:
        if y < h:
            y = y + 1
            n = n - 1
        else:

            x = x + 1
            y = 1
            n = n - 1

    if x < 10:
        print(str(y)+'0'+str(x))
    else:
        print(str(y)+str(x))
