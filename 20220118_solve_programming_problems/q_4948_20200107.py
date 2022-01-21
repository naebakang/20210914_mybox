import sys
a = [True]*123457*2
a[0] = False
a[1] = False
for i in range(2, len(a)+1):
    for ii in range(2, int(len(a)/2)+1):
        if i*ii > len(a):
            break
        else:
            a[i*ii] = False
while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        b = 0
        for i in range(n, 2*n+1):
            if a[i] == True:
                b += 1
    print(b)