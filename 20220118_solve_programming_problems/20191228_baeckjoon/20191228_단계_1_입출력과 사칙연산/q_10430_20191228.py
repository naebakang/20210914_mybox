a, b, c = map(int, input().split())
if 2 <= a <= 10000 and 2 <= b <= 10000 and 2 <= c <= 10000:
    print((a+b)%c)
    print((a%c + b%c)%c)
    print(a*b%c)
    print((a%c*b%c)%c)
