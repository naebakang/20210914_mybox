# File encoding: UTF-8


def main(num_of_iter, principal, rate):
    if num_of_iter == 0:
        return
    else:
        principal = principal + rate*principal
        num_of_iter -= 1
        print(principal)
        print(num_of_iter)

    main(num_of_iter, principal, rate)


# num_of_iter = 30*2
# principal = 20000000
# rate = 0.1

num_of_iter = 12
principal = 1000000
rate = 0.09

main(num_of_iter, principal, rate)

anw = principal*(1+rate)**num_of_iter

anw2 = principal*(1+rate*num_of_iter + rate**(num_of_iter-1)*num_of_iter + rate**num_of_iter)
a=5
