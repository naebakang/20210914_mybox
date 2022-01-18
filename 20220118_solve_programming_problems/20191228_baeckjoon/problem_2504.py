# File encoding: UTF-8

import sys

st = str(sys.stdin.readline())
st = st.strip('\n')

anw = 0
# validate1
for i in st:
    if i == '(' or i == ')' or i == '[' or i == ']':
        anw = 1
    else:
        anw = 0
        break

# validate2
if anw == 0:
    pass
else:
    check_list = []
    for i in st:
        if i == '(' or i == '[':
            check_list.append(i)
        elif i == ')':
            if check_list[-1] == '(':
                del check_list[-1]
            else:
                anw = 0
        elif i == ']':
            if check_list[-1] == '[':
                del check_list[-1]
            else:
                anw = 0
        else:
            anw = 0

    if len(check_list) == 0:
        anw = 1
    else:
        anw = 0

# start&iteration
if anw == 0:
    pass
else:
    # start
    change_list = []
    for i in st:
        if i == '(':
            change_list.append(i)
        elif i == '[':
            change_list.append(i)
        elif i == ')':
            if change_list[-1] == '(':
                del change_list[-1]
                change_list.append(2)
            else:
                change_list.append(i)
        elif i == ']':
            if change_list[-1] == '[':
                del change_list[-1]
                change_list.append(3)
            else:
                change_list.append(i)

    # iteration
    while 2 < len(change_list):
        next_list = []
        for i in range(len(change_list)):
            if type(change_list[i]) == int:
                if type(change_list[i-1]) == int:
                    del next_list[-1]
                    next_list.append(change_list[i-1]+change_list[i])
                else:
                    next_list.append(change_list[i])
            else:
                next_list.append(change_list[i])
        change_list = next_list

        next_list = []
        for i in range(len(change_list)):
            if change_list[i] == ')':
                if type(change_list[i-1]) == int:
                    del next_list[-1]
                    del next_list[-1]
                    next_list.append(change_list[i-1]*2)
                else:
                    next_list.append(change_list[i])

            elif change_list[i] == ']':
                if type(change_list[i-1]) == int:
                    del next_list[-1]
                    del next_list[-1]
                    next_list.append(change_list[i-1]*3)
                else:
                    next_list.append(change_list[i])
            else:
                next_list.append(change_list[i])
        change_list = next_list

    # answer
    anw = sum(change_list)
print(int(anw))


# (()[[]])([])
# 28
