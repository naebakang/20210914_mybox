# File encoding: UTF-8

import numpy

error1 = [-100, 3200, 700, -2800, 500]
error2 = [-300, 2400, 1300, -2800, -800]

# simultaneous equation
# 5*c1 + c2*sum(error2) = sum(error1)
square = []
multiplication = []
for i in range(len(error1)):
    square.append(error2[i]**2)
    multiplication.append(error2[i]*error1[i])

# c1*sum(error2) + c2*sum(error2)**2 = sum(multiplication)
c2 = 16120000 / 16012000
c1 = (sum(error1) - c2*sum(error2)) / 5

# determinant
x = numpy.array([[error2[0], 1],
                 [error2[1], 1],
                 [error2[2], 1],
                 [error2[3], 1],
                 [error2[4], 1]])

y = numpy.array([[error1[0]],
                 [error1[1]],
                 [error1[2]],
                 [error1[3]],
                 [error1[4]]])

square_matrix = numpy.dot(x.T, x)
square_matrix_inv = numpy.linalg.inv(square_matrix)
pseudo_x = numpy.dot(square_matrix_inv, x.T)
ab = numpy.dot(pseudo_x, y)

compare_1 = c2 - ab[0][0]
compare_2 = c1 - ab[1][0]

print(compare_1)
print(compare_2)

# numpy - least square method
a, resid, rank, s = numpy.linalg.lstsq(x, y, rcond=None)

compare_1 = c2 - a[0][0]
compare_2 = c1 - a[1][0]

print(compare_1)
print(compare_2)
