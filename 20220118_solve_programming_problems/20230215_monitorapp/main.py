# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def f(s):
    ans = ''

    button = {
        "1": [".", "Q", "Z"],
        "2": ["A", "B", "C"],
        "3": ["D", "E", "F"],
        "4": ["G", "H", "I"],
        "5": ["J", "K", "L"],
        "6": ["M", "N", "O"],
        "7": ["P", "R", "S"],
        "8": ["T", "U", "V"],
        "9": ["W", "X", "Y"],
    }

    list_split = []
    strr = ""
    for idx, num in enumerate(s):
        if num == "0":
            if strr != "":
                list_split.append(strr)
                strr = ""
        else:
            if len(strr) == 0:
                strr += num
                if len(s)-1 == idx:
                    list_split.append(strr)
            elif 1 <= len(strr) < 3:
                if strr[-1] == num:
                    strr += num
                    if len(strr) == 3:
                        list_split.append(strr)
                        strr = ""
                else:

                    list_split.append(strr)
                    strr = num
                    if len(s) - 1 == idx:
                        list_split.append(strr)

    for i in list_split:
        key = i[0]
        idx = len(i)-1
        answer_str = button[key][idx]
        ans += answer_str

    return ans  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    # solution('44335550555666')
    #
    # solution('9666775553')

    f('2220281')

