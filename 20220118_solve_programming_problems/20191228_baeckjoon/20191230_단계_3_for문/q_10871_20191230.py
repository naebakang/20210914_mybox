import sys
n, x = map(int, sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
b = []
for i in range(n):
    if x > a[i]:
        b.append(str(a[i]))
print(' '.join(b))
