import sys
a = []
for i in range(3):
    a.append(int(sys.stdin.readline()))
r = str(a[0]*a[1]*a[2])
c = 0
ans = []
for i in range(10):
    for ii in range(len(r)):

        if str(i) == r[ii]:
            c += 1
    ans.append(c)
    c = 0
for i in range(len(ans)):
    print(ans[i])

##more
# count 사용
r = list(map(int, str(a[0]*a[1]*a[2])))
for i in range(10):
    print(r.count(i))
