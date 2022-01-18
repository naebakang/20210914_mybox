import sys
c = int(sys.stdin.readline())
for i in range(c):
    print(sum(map(int, sys.stdin.readline().split())))
