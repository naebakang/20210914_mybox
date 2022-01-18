import sys
c = int(sys.stdin.readline())
for i in range(c):
    a = list(map(int, sys.stdin.readline().split()))
    p = 0
    for ii in range(1, a[0]+1):
        if a[ii] > sum(a[1:])/a[0]:
            p += 1
    print(format(p/a[0], '.3%'))
