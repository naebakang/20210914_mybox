a, b = map(str, input().split())
if float(a)%1 == 0 and float(b)%1 == 0 and 1 <= int(a) and int(b) < 10000:
    print(int(a)+int(b))
    print(int(a)-int(b))
    print(int(a)*int(b))
    print(int(a)//int(b))
    print(int(a)%int(b))
