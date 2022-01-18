import sys
t = int(sys.stdin.readline())
for i in range(1, t+1):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #%s: %s + %s = %s' % (i, a, b, a+b))
