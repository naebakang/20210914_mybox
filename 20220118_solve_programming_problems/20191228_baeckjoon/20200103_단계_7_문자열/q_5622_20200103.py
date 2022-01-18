import sys, string
a = sys.stdin.readline().strip()
b = string.ascii_uppercase
c = []
for i in a:
    d = 0
    if b.index(i) < 3:
        d = 3
    elif 3 <= b.index(i) < 6:
        d = 4
    elif 6 <= b.index(i) < 9:
        d = 5
    elif 9 <= b.index(i) < 12:
        d = 6
    elif 12 <= b.index(i) < 15:
        d = 7
    elif 15 <= b.index(i) < 19:
        d = 8
    elif 19 <= b.index(i) < 22:
        d = 9
    else:
        d = 10
    c.append(d)
print(sum(c))
