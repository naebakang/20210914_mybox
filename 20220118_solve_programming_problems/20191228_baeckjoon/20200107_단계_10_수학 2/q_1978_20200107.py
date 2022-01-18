import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = []
for i in range(1001):
    b.append(True)
for i in range(2, 1001):
    for ii in range(2, 501):
        if i*ii > 1000:
            break
        else:
            b[i*ii] = False
b[0] = False
b[1] = False
c = 0
for i in a:
    if b[i] == True:
        c += 1
print(c)
