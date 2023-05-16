# File encoding: utf8

import pandas
import matplotlib.pyplot as plt
import math
import numpy


# github #############################################################################################################
profits = [0.1, 0.2, -0.3, 0.2, -0.1]
profits = pandas.DataFrame(profits)

# 최종 수익률과 존버 수익률 비교
net_profit = (profits+1).cumprod()
hodl = [0.1, 0.2, -0.3, 0.2, -0.1]

# cagr 계산
total_days = 5
# cagr = 100 * (net_profit[-1] - 1)**(365 / total_days) - 1

# # drawdown 계산
# local_best = 0.0
# DD = dict(ts=[], dd=[])
# for ts, p in net_profit.iteritems():
#     if p > local_best:
#         local_best = p
#     _DD = (p - local_best) / local_best
#     DD['ts'].append(ts)
#     DD['dd'].append(_DD)
#
# DD = pd.DataFrame(DD, index=DD['ts'], columns=['dd'])
# MDD = 100 * DD['dd'].min()

# 수익 거래, 손실 거래 수 계산
wins = profits[profits >= 0.0].count()
loses = profits[profits < 0.0].count()

net_profit.plot(style='.-', title='Strategy performance vs HODL')
# _ = hodl.plot()
plt.show()
print('총 거래 수: {}'.format(len(profits)))
# print('승률: {:.0f}%'.format(100 * (wins / (wins+loses))))
# print('최종 자산 증가율: {:.0f}배'.format(net_profit[-1]))
# print('존버: {:.0f}배'.format(df['C'][-1] / df['C'][0]))
# print('CAGR: {:.0f}%'.format(cagr))
# print('MDD: {:.0f}%'.format(MDD))

plt.hist(profits, bins=100)
plt.show()


def kelly(profits):
    N = len(profits)
    result = []
    stop = False
    i = 0
    max_v = 0.0
    max_f = 0.0
    while True:
        f = 0.01 * i
        v = 0.0
        for profit in profits:
            if (1 + f * profit < 0):
                stop = True
                break
            v += (1 / N) * math.log10(1 + f * profit)

        if v > max_v:
            max_v = v
            max_f = f

        if stop:
            break
        result.append((f, v))
        i += 1

    F = [v[0] for v in result]
    V = [v[1] for v in result]

    return max_f, F, V


max_f, F, V = kelly(profits.values)
plt.plot(numpy.array(F), numpy.array(V), '-', linewidth=1)
plt.show()
print('최적 베팅 비율: {:.2f}'.format(max_f))
