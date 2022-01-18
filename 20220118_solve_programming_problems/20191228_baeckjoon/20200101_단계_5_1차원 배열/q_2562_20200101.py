import sys
a = []
for i in range(9):
    a.append(int(sys.stdin.readline()))
b = 0
for i in range(9):
    if a[i] == max(a):
        break
    b += 1
print(max(a))
print(b+1)
