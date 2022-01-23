# File encoding: UTF-8

from matplotlib import pyplot

y = []
x = 5
for i in range(100):
    y.append(x)
    x = 105 / (x+7)

# graph
pyplot.figure('degree=1')
pyplot.plot(y, 'ob', label='p')

pyplot.title('polynomial function of one variable')
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.grid(True)
pyplot.legend(loc='upper right')
# pyplot.axis([-1, 100, 0.65331, 0.653315])
