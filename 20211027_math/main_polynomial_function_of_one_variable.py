# File encoding: UTF-8

import numpy
from matplotlib import pyplot


# function
start = -10
end = 10

x = numpy.linspace(start, end, 100, endpoint=True, retstep=False, dtype=None, axis=0)
fx = x + 2
fx2 = (x**2 - x - 2)
fx3 = 1/4*(x**3 + 3*x**2 - 6*x - 8)
fx4 = 1/14*(x**4 + 4*x**3 - 24*x**2 - x + 9)
fx5 = 1/20*(x**5 + 7*x**4 - 5*x**3 - 57*x**2 + 39*x + 72)


# graph
pyplot.figure('degree=1')
pyplot.plot(x, fx, 'ob', label='degree=1')

pyplot.title('polynomial function of one variable')
pyplot.xlabel('x')
pyplot.ylabel('fx')
pyplot.grid(True)
pyplot.legend(loc='upper right')
pyplot.axis([-20, 20, -20, 20])


pyplot.figure('degree=2~', figsize=(10, 9))
pyplot.title('polynomial function of one variable')

pyplot.subplot(2, 2, 1)
pyplot.plot(x, fx2, 'or', label='degree=2')
pyplot.xlabel('x')
pyplot.ylabel('fx2')
pyplot.grid(True)
pyplot.legend(loc='upper right')
pyplot.axis([start, end, start, end])

pyplot.subplot(2, 2, 2)
pyplot.plot(x, fx3, 'oy', label='degree=3')
pyplot.xlabel('x')
pyplot.ylabel('fx3')
pyplot.grid(True)
pyplot.legend(loc='upper right')
pyplot.axis([start, end, start, end])

pyplot.subplot(2, 2, 3)
pyplot.plot(x, fx4, 'og', label='degree=4')
pyplot.xlabel('x')
pyplot.ylabel('fx4')
pyplot.grid(True)
pyplot.legend(loc='upper right')
pyplot.axis([-40, 40, -40, 40])

pyplot.subplot(2, 2, 4)
pyplot.plot(x, fx5, 'o', label='degree=5')
pyplot.xlabel('x')
pyplot.ylabel('fx5')
pyplot.grid(True)
pyplot.legend(loc='upper right')
pyplot.axis([-20, 20, -20, 20])




