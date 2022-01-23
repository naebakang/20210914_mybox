# File encoding: UTF-8

import numpy
from matplotlib import pyplot

"""
20201207, 최초생성, 블로그에 경사하강법에 대한 글에 넣을 그래프 그리기
"""


def f_x(domain):
    x = domain
    # y = (x**4 + x**3 - 13*x**2 - x + 12)/14 + 0.5
    # y = (x + 4) * (x + 1) * (x - 1) * (x - 3) / 14 + 0.5

    # y = x**5 - 4*x**4 - 18*x**3 + 64*x**2 + 17*x - 60
    y = (x + 4) * (x + 1) * (x - 1) * (x - 3) * (x - 5)

    return y


def prime_f_x(domain):
    x = domain
    # prime_y = (4*x**3 + 3*x**2 - 26*x - 1)/14
    prime_y = 5*x**4 - 16*x**3 - 54*x**2 + 128*x + 17

    return prime_y


def gradient_descent(x0, alpha):
    dy_dx0 = prime_f_x(domain=x0)
    x_n_p_1 = x0 - alpha*dy_dx0

    return x_n_p_1


x = numpy.arange(-2.5, 5.5, 0.05)
y = f_x(domain=x)
iterate = 5
alpha = 0.008

ex1_x = []
ex1_y = []
x0 = -2.0
for i in range(iterate):
    ex1_x.append(x0)
    yp = f_x(domain=x0)

    x0 = gradient_descent(x0=x0, alpha=alpha)
    ex1_y.append(yp)

ex2_x = []
ex2_y = []
x0 = 3.0
for i in range(iterate):
    ex2_x.append(x0)
    yp = f_x(domain=x0)

    x0 = gradient_descent(x0=x0, alpha=alpha)
    ex2_y.append(yp)


# graph
pyplot.figure('NaeBaKang')
pyplot.plot(x, y, '-')
pyplot.plot(ex1_x, ex1_y, 'ro', label='ex1')
pyplot.plot(ex2_x, ex2_y, 'b^', label='ex2')

pyplot.title('Gradient descent')
pyplot.xlabel('x')
pyplot.ylabel('f(x)')
pyplot.grid(True)
pyplot.legend(loc='upper right')
# pyplot.axis([-1, 100, 0.65331, 0.653315])
pyplot.show()
