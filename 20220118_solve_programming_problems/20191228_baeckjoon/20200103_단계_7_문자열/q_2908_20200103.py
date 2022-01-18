import sys
a, b = map(str, sys.stdin.readline().split())
print(max([int(a[::-1]), int(b[::-1])]))

