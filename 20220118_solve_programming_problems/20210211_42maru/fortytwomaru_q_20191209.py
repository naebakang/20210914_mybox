a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 19, 20]
b = [3, 5, 6, 8, 10, 11, 13, 15, 16, 17, 19,]
c = [5, 9, 10, 14, 16, 18]

#문제: a, b, c 리스트 모두에서 겹치는 숫자가 무엇인지 알아내도록 코드를
#작성하시오



#나의 답안
d = []
for i in range(len(c)):
    for ii in range(len(b)):
        if c[i] == b[ii]:
            d.append(c[i])
e = []
for i in range(len(d)):
    for ii in range(len(a)):
        if d[i] == a[ii]:
            e.append(d[i])
print(e)



#제출자가 원하는 답안
x = 0
y = 0
z = 0
