import sys
while 1:
    try:
        a, b = map(int, sys.stdin.readline().split())
    except:
        break
    print(a+b)
