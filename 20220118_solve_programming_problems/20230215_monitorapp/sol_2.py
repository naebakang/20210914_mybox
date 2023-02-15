# File encoding: utf8


def f(n, v):
    max_v = max(v)
    max_idx = v.index(max_v)

    if n-1 == max_idx:
        v.remove(max_v)
        min_v = max(v)
        ans = int(min_v-max_v)
    else:
        list_split = v[max_idx+1:]

        min_v = min(list_split)

        ans = int(max_v-min_v)

    return ans  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    f(10, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3])

    f(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
