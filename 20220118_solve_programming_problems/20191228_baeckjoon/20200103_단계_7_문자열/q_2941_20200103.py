import sys
a = sys.stdin.readline().strip()
b = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
c = []
d = 0
for i in b:
    c.append(a.count(i))
for i in b:
    a = a.replace(i, '',c[d])
    d += 1
print(sum(c)+len(a)-c[2])
