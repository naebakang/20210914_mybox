import sys
n = int(sys.stdin.readline())
a = 0
for i in range(1, n+1):
    if i < 10:
        a += 1
    elif 10 <= i < 100:
        a += 1
    elif 100 <= i < 1000:
        if (i//100 - i%100//10) == (i%100//10 - i%100%10%10):
            a += 1
        else:
            pass
    else:
        pass
print(a)
