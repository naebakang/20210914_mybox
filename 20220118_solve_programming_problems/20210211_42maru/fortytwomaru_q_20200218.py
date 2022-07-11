# 문제: a, b, c 리스트 모두에서 겹치는 숫자가 무엇인지 알아내도록 코드를 작성하시오

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 19, 20]
b = [3, 5, 6, 8, 10, 11, 13, 15, 16, 17, 19]
c = [5, 9, 10, 14, 16, 18]


print(len(a))
print(len(b))
print(len(c))


#나의 답안
step1 = 0
d = []
for i in range(len(c)):
    for ii in range(len(b)):
        step1 += 1
        if c[i] == b[ii]:
            d.append(c[i])
e = []
for i in range(len(d)):
    for ii in range(len(a)):
        step1 += 1
        if d[i] == a[ii]:
            e.append(d[i])
print(e)
print('step1 = %s' % step1)


#제출자가 원하는 답안
step2 = 0
f = []
x = 0
y = 0
z = 0
while z < len(c):
    while y < len(b):
        step2 += 1
        if c[z] == b[y] == a[x]:
            f.append(c[z])
            x = x + 1
            y = y + 1
            z = z + 1
            
        elif c[z] != b[y] == a[x]:
            y = y + 1

        elif c[z] == b[y] != a[x]:
            x = x + 1

        elif c[z] != b[y] != a[x]:
            y = y + 1
            x = x + 1

    x = 0
    y = 0
    z = z + 1
print(f)
print('step2 = %s' % step2)

#2
step3 = 0
key_value1 = 21*[False]
for i in c:
    step3 += 1
    key_value1[i] = True
key_value2 = 21*[False]
for i in b:
    step3 += 1
    key_value2[i] = True
key_value3 = 21*[False]
for i in a:
    step3 += 1
    key_value3[i] = True
answer = []
for i in range(21):
    step3 += 1
    if key_value1[i] == key_value2[i] == key_value3[i] == True:
        answer.append(i)
print(answer)
print('step3 = %s' % step3)

# 20220711, 이승현 매니저 아이디어
list_total = [a, b, c]
dic_total = {}
step4 = 0
anw4 = []
for i in list_total:
    for ii in i:
        if str(ii) in dic_total:
            dic_total[str(ii)] += 1
        else:
            dic_total[str(ii)] = 0

        if dic_total[str(ii)] == 2:
            anw4.append(ii)
        step4 += 1

print(anw4)
print("step4: {}".format(step4))
