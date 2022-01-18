import sys, string
a = sys.stdin.readline()
b = string.ascii_letters
d = []
for i in b:
    c = 0
    for ii in a:
        if i == ii:
            c += 1
    d.append(c)
e = []
for i in range(int(len(b)/2)):
    e.append(int(d[i])+int(d[i+int(len(b)/2)]))
if sorted(e, reverse=True)[0] == sorted(e, reverse=True)[1]:
    print('?')
else:
    print(b[e.index(max(e))+26])
