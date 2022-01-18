import sys
n = int(sys.stdin.readline())
if n < 10:
    a = int(str(n)+str(n))
    d = 1
    while 1:
        if a == n :
            break
        elif a < 10:
            b = a
            c = a
            a = int(str(b) + str(c))
        elif a >= 10:
            b = str(a)[1]
            if int(str(a)[0]) + int(str(a)[1]) < 10:
                c = int(str(a)[0]) + int(str(a)[1])
            else:
                c = int(str(int(str(a)[0]) + int(str(a)[1]))[1])
            a = int(str(b) + str(c))
        d = d + 1
elif n >= 10:
    e = str(n)[1]
    if int(str(n)[0]) + int(str(n)[1]) < 10:
        f = str(int(str(n)[0]) + int(str(n)[1]))
    else:
        f = str(int(str(n)[0]) + int(str(n)[1]))[1]
    a = int(e+f)
    d = 1
    while 1:
        if a == n :
            break
        elif a < 10:
            b = a
            c = a
            a = int(str(b) + str(c))
        elif a >= 10:
            b = str(a)[1]
            if int(str(a)[0]) + int(str(a)[1]) < 10:
                c = int(str(a)[0]) + int(str(a)[1])
            else:
                c = int(str(int(str(a)[0]) + int(str(a)[1]))[1])
            a = int(str(b) + str(c))
        d = d + 1
print(d)

##more
#수학을 좀 더 활용하면 더 짧게 코딩 할 수 있다.
import sys
n = int(sys.stdin.readline())
a = n
b = 0
while 1:
    c = (n%10)*10
    d = (n//10 + n%10)%10
    n = c + d
    b += 1
    if n == a:
        break
print(b)
