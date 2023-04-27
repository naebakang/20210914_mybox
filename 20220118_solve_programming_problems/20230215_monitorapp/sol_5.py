# File encoding: utf8


def f(N, bus_stop):
    ans = []
    ans_split = []
    for row in range(1, N+1):
        for col in range(1, N+1):
            list_dist = []
            for bus in bus_stop:
                x = abs(bus[0] - row)
                y = abs(bus[1] - col)
                dist = x+y  # (x**2 + y**2)**(1/2)
                list_dist.append(dist)

            bus_idx = list_dist.index(min(list_dist))
            bus_x = bus_stop[bus_idx][0]
            bus_y = bus_stop[bus_idx][1]

            x = abs(bus_x-row)
            y = abs(bus_y - col)
            ans_split.append(x+y)

    for i in range(0, len(ans_split), N):
        ans.append(ans_split[i:i + N])

    return ans


if __name__ == '__main__':
    f(3, [[1, 2]])  # [[1,0,1], [2,1,2], [3,2,3]]

    f(3, [[1, 2], [3, 3]])  # [[1,0,1], [2,1,1], [2,1,0]]
