t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if 0 < a and b < 10:
        print(a+b)

##more
#input() 보다 sys.stdin.readline()이 속도가 더 빠르다.
import sys
t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    if 0 < a and b < 10:
        print(a+b)
