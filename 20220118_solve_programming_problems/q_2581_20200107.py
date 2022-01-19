import sys
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = [True]*10001
a[0] = False
a[1] = False
for i in range(2, 10001):
    for ii in range(2, 5001):
        if i*ii > 10000:
            break
        else:
            a[i*ii] = False
b = []
for i in range(m, n+1):
    if a[i] == True:
        b.append(i)
print(sum(b))
print(min(b))
