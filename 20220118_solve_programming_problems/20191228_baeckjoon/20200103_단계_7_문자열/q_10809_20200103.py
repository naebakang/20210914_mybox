import sys, string
s = sys.stdin.readline().strip('\n')
a = []
for i in range(len(string.ascii_lowercase)):
    try:
        a.append(str(s.index(string.ascii_lowercase[i])))
    except:
        a.append('-1')
print(' '.join(a))


