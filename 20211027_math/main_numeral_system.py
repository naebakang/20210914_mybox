# File encoding: UTF-8
# any_base, decimal_number is INT
# 0 < any_base, decimal_number < 10,000


def get_any_base_numeral_system_from_decimal(any_base, decimal_number):
    while_check = True
    n = 0
    while while_check:
        if any_base**n <= decimal_number:
            n += 1
        else:
            while_check = False

    remainder = decimal_number
    for i in range(n-1, -1, -1):
        print(remainder//any_base**i)
        remainder = remainder % any_base**i


get_any_base_numeral_system_from_decimal(any_base=16, decimal_number=43263)
