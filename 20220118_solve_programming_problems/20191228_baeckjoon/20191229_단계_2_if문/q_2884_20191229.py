h, m = map(int, input().split())
if 0 <= h <=23 and 0 <= m <= 59:
    t = h*60 + m
    st = t - 45
    if st < 0:
        t = t + 24*60
        st = t - 45
    print(st//60, st%60)
