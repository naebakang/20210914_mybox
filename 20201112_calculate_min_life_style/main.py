# File encoding: UTF-8


def get_cost(month_eat, month_warm, inflation_rate, want_period):
    n = 0
    a = 1 + inflation_rate/100
    b = 0
    c = 0
    while n < want_period:
        b = a**n
        c += b
        n += 1

    cost = (month_eat + month_warm)*12*c
    cost = int(cost)
    print('%s년 동안 필요한 금액: %s만원' % (want_period, cost))


def get_period(have_money, month_eat, month_warm, inflation_rate):
    remain_money = have_money
    num = 0
    n = 1
    nn = 0
    while 0 < remain_money:
        while n < 13:
            remain_money = remain_money - (month_eat + month_warm)*(1+inflation_rate/100)**nn
            if remain_money < 0:
                break
            num += 1

        nn += 1

    print('%s만원으로 버틸 수 있는 기간: %s년 %s개월' % (have_money, num//12, num % 12))


if __name__ == '__main__':
    month_eat = 30  # 만원
    month_warm = 40  # 만원
    inflation_rate = 1  # %
    want_period = 5  # 년
    get_cost(month_eat=month_eat, month_warm=month_warm, inflation_rate=inflation_rate, want_period=want_period)

    have_money = 3000  # 만원
    month_eat = 30
    month_warm = 40
    inflation_rate = 1
    get_period(have_money=have_money, month_eat=month_eat, month_warm=month_warm, inflation_rate=inflation_rate)
