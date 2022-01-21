import sys
x = int(sys.stdin.readline())
a = 0
for i in range(1, 10000):
    a = a + i
    if x <= a:
        break
if i%2 == 0:
    print(str(i-(i-(x-(a-i)))) + '/' + str(i-(x-(a-i)-1)))
else:
    print(str(i-(x-(a-i)-1))+'/'+str(i-(i-(x-(a-i)))))
