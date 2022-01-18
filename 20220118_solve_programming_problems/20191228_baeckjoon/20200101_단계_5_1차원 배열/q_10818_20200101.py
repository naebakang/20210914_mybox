import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = 0
chk1 = 0
while 1:
    for i in range(n):
        if b - a[i] == 0:
            min = b
            chk1 = 1
            break
    b += 1
    if chk1 == 1:
        break
b = 0
while 1:
    for i in range(len(a)):
        if b - a[i] == 0:
            a.remove(a[i])
            break
    if len(a) == 0:
        max = b
        break
    b += 1
print(' '.join([str(min), str(max)]))

##more
#시간 단축
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
print(' '.join([str(a[0]), str(a[n-1])]))

##more more
# * 의 사용 및 더 시간 다축(*는 파라미터를 몇 개 받을지 모르는 경우 사용한다.)
import sys
_,*v=map(int,sys.stdin.read().split())
print(min(v),max(v))
