import sys
t = int(sys.stdin.readline())
def key(n):
    return n*(n+1)/2
for i in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    a = 0
    for i in range(k):
        for ii in range(1, n+1):
            b = key(ii)
            a = a + b
    print(a)

