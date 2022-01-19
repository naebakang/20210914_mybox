import sys
m, n = map(int, sys.stdin.readline().split())
a = [True]*1000001
a[0] = False
a[1] = False
for i in range(2, len(a)):
    for ii in range(2, 500001):
        if i*ii > 1000000:
            break
        else:
            a[i*ii] = False

for i in range(m, n+1):
    if a[i] == True:
        print(i)
