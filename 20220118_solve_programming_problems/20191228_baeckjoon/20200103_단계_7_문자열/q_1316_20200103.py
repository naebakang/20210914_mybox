import sys, string
a = string.ascii_lowercase
n = int(sys.stdin.readline())
e = 0
for i in range(n):
    c = 0
    d = 0
    b = sys.stdin.readline().strip()
    for ii in a:
        c = b.count(ii)
        for iii in range(c):
            if b[b.index(ii)+iii] != ii:
                d += 1
    if d >= 1:
        e += 1
print(n-e)

##more
#sorted의 활용
import sys
n = int(sys.stdin.readline())
c = 0
for i in range(n):
    b = sys.stdin.readline().strip()
    if list(b) == sorted(b, key=b.find):
        c += 1
print(c)
