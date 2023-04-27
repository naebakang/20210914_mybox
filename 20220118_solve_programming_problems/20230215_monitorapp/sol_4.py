# File encoding: utf8


def f(n):
    global strr
    list_num = ["4", "13"]
    list_s = []
    strr = ""

    def app(nn):
        for i in range(nn):
            for ii in list_num:
                strr += ii
            list_s.append(strr)

    for i in range(n):
        app(i)


    return list_s  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    f(1)  # 4

    f(2)  # 13

    f(3)  # 44
