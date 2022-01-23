# File encoding: UTF-8

import random


def make_security_number(length):
    special_str = []
    for i in range(33, 39):
        special_str.append(chr(i))
    for i in range(40, 44):
        special_str.append(chr(i))
    special_str.append(chr(58))
    special_str.append(chr(60))
    special_str.append(chr(62))
    special_str.append(chr(63))
    special_str.append(chr(94))
    special_str.append(chr(95))
    special_str.append(chr(123))
    special_str.append(chr(125))
    special_str.append(chr(126))

    number_str = []
    for i in range(48, 58):
        number_str.append(chr(i))

    capital_str = []
    for i in range(65, 91):
        capital_str.append(chr(i))

    small_str = []
    for i in range(97, 123):
        small_str.append(chr(i))

    total_str = special_str + number_str + capital_str + small_str
    number_small_str = number_str + small_str

    security_number = []
    for i in range(length):
        if i == 0 or i == length-1:
            security_number.append(random.choice(number_small_str))

        else:
            security_number.append(random.choice(total_str))

    return security_number


print(make_security_number(length=10))
ord("'")
