import sys
a = []
for i in range(10):
    a.append(int(sys.stdin.readline()))
b = []
for i in range(len(a)):
    b.append(a[i]%42)
print(len(set(b)))
