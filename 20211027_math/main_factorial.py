# File encoding: UTF-8


def factorial(x):
    if x < 0:
        raise ValueError

    elif x == 0:
        return 1

    elif type(x) != int:
        raise ValueError

    else:
        return x * factorial(x - 1)


n = 10
x = 0
acc = 0.55
p = 0

for x in range(n+1):
    p += factorial(n)/factorial(x)/factorial(n-x) * acc**x * (1-acc)**(n-x)
    print(x)
    print(factorial(n)/factorial(x)/factorial(n-x) * acc**x * (1-acc)**(n-x))
    print('')

xx = 500000
for i in range(10):
    xx = xx * 1.02

print(xx)
