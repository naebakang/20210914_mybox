import sys
n = int(sys.stdin.readline())
chk = 0
for i in range(2000):
    if chk == 1:
        break
    for ii in range(1001):
        if chk == 1:
            break
        elif n - 3*i - 5*ii == 0:
            print(i + ii)
            chk = 1
if chk != 1:
    print(-1)
