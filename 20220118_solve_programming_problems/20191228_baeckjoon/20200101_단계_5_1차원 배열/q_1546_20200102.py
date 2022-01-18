import sys
a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
print(sum(b)/len(b)/max(b)*100)
