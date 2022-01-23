# File encoding: UTF-8

"""
a, b, c 3개 리스트 모두에서 공통인 수를 갇는 리스트를 생성하고 출력하라.
"""

a = [2, 5, 6, 7, 8, 13, 24, 46, 76, 88, 89, 93, 98]
b = [5, 8, 9, 13, 25, 38, 39, 46, 49, 93]
c = [7, 8, 13, 14, 15, 16, 46, 93]

d = []
for i in c:
    for ii in b:
        if i == ii:
            for iii in c:
                if i == iii:
                    d.append(i)

print(d)
