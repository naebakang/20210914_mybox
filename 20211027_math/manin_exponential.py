# File encoding: utf8

import numpy
import math
from matplotlib import pyplot

start = 0.5
end = 1
x = numpy.linspace(start, end, 100, endpoint=True, retstep=False, dtype=None, axis=0)
a = numpy.linspace(0.001, 0.099, 1, endpoint=True, retstep=False, dtype=None, axis=0)
for ii in a:
    y = []
    for i in x:
        y.append(math.pow(0.028, i-0.17))
    if 15 < y[0]/y[-1]:
        print(ii)
        break


# graph
pyplot.figure('degree=1')
pyplot.plot(x, y, 'ob', label='degree=1')

pyplot.title('polynomial function of one variable')
pyplot.xlabel('x')
pyplot.ylabel('fx')
pyplot.grid(True)
pyplot.legend(loc='upper right')
# pyplot.axis([-0.1, 2, -0.1, 10])

print(y[0])
print(y[-1])
print(y[0]/y[-1])


