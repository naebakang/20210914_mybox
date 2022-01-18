a, b, c = map(int, input().split())
if 1<= a <= 100 and 1<= b <= 100 and 1<= c <= 100:
    if a == b:
        print(a)
    elif a == c:
        print(a)
    elif c == b:
        print(b)
    elif a != b != c:
        if b < a < c or b > a > c:
            print(a)
        elif a < b < c or a > b >c:
            print(b)
        elif a < c < b or a > c > b:
            print(c)
