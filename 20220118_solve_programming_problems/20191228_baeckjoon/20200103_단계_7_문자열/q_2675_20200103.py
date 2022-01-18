import sys
t = int(sys.stdin.readline())
for i in range(t):
    r, s = map(str, sys.stdin.readline().split())
    p = ''
    for i in s:
        p = p + i*int(r)
    print(p)
