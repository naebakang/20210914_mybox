# File encoding: UTF-8

from sympy import Symbol, solve

y = Symbol('y')
a = Symbol('a')

eq_1 = y/a - 39950
eq_2 = y/(a+26990) - 28997

anw = solve((eq_1, eq_2), dict=True)

ori_1 = anw[0][y] / (anw[0][a])
ori_2 = anw[0][y] / (anw[0][a]+26990)
new = anw[0][y] / (anw[0][a]+46377)

print(float(ori_1))
print(float(ori_2))
print(float(new))
