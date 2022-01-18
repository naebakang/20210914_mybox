import sys
a = int(sys.stdin.readline())
b = []
for i in range(a):
    b.append(sys.stdin.readline().rstrip('\n'))
for i in range(a):
    score = []
    point = 0
    for ii in range(len(b[i])):
        if b[i][ii] == 'O':
            point += 1
            score.append(point)
        else:
            point = 0
    print(sum(score))
