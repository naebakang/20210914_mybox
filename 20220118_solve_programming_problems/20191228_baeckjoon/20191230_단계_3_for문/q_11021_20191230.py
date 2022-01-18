import sys
t = int(sys.stdin.readline())
for i in range(1, t+1):
    n = sum(map(int, sys.stdin.readline().split()))
    print('Case #%s: %s' % (i, n))
