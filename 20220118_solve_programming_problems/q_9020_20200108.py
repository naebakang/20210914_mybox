import sys
a = [True]*10001
a[0] = False
a[1] = False
for i in range(2, len(a)):
    for ii in range(2, int(len(a)/2)+1):
        if i*ii >= len(a):
            break
        else:
            a[i*ii] = False
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    b = []
    for ii in range(2, n):
        if a[ii] == True:
            b.append(ii)
    c = []
    xx = 0
    for ii in range(len(b)):
        if b[ii]*2 == n:
            print(str(b[ii])+' '+str(b[ii]))
            xx = 1
        else:
            for iii in range(1, len(b)):
                if b[ii]+b[iii] == n:
                    c.append(b[ii])
                    c.append(b[iii])
    c = list(set(c))
    d = []
    for ii in range(0, len(c), 2):
        if c[ii+1]-c[ii] > 0:
            d.append(c[ii+1]-c[ii])
    e = sorted([c[d.index(min(d))], c[d.index(min(d))+1]])
    if xx != 1:
        print(' '.join(map(str, e)))