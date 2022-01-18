a, b = map(str, input().split())
if float(a)%1 == 0 and float(b)%1 == 0 and 0 < int(a) and int(b) < 10:
    print(int(a)*int(b))
