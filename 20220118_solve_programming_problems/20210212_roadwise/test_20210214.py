# File encoding: UTF-8

import numpy

"""
20210202에 주식회사 로드와이즈로 면접을 보러갔다. 면접에서 30분 동안 필기시험을 봤어야 했으며,
필기시험 중 풀지 못 한 코딩 문제를 여기에 기록해둔다.

a 리스트에는 17개의 원소가 있다. 이를 내림 차순으로 배열 한 후, 5x5 행렬에서 모레시계 모양을 이루도록 하라.

"""

a = [100, 89, 2, 5, 110, 6, 7, 111, 8, 93, 13, 24, 46, 76, 88, 98, 103]

# 1
b = len(a) - 1
for i in range(b):
    c = 0
    for ii in range(b):
        d = c + 1
        if a[c] < a[d]:
            e = a[c]
            a[c] = a[d]
            a[d] = e

        c = c + 1

    b = b - 1

print(a)


# 2
f = numpy.zeros((5, 5), dtype=int)
absolute_index = 0
start = 0
end = 5
for row in range(5):
    for column in range(start, end):
        f[row, column] = a[absolute_index]

        absolute_index = absolute_index + 1

    if row < 2:
        start = start + 1
        end = end - 1

    else:
        start = start - 1
        end = end + 1

print(f)
