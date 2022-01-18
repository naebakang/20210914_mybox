def selfnum(n):
    if n < 100:
        return n + n//10 + n%10
    elif 100 <= n < 1000:
        return n + n//100 + n%100//10 + n%100%10
    elif 1000 <= n < 10000:
        return n + n//1000 + n%1000//100 + n%1000%100//10 + n%1000%100%10
a = []
for i in range(1, 10000):
    a.append(selfnum(i))
b = list(range(1, 10001))
for i in a:
    if i in b:
        b.remove(i)
for i in range(len(b)):
    print(b[i])

##more
#더 단순하게
def selfnum(n):
    return selfnum(n//10) + n%10 if n else 0
a = []
for i in range(20000):
    a.append(0)
for i in range(10000):
    a[i+selfnum(i)] = 1
    if a[i] == 0:
        print(i)

##more
#다른 수학적 사고, 미완성
def selfnum(n):
    if n%1001%101%11%2 == 0:
        return True
for i in range(10000):
    if selfnum(i) == True:
        pass
    else:
        print(i)
