import sys
n = int(sys.stdin.readline())
a = 1
for i in range(1000000000//6+1):
    a = a + 6*i
    if n <= a:
        print(i+1)
        break
