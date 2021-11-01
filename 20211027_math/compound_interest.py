# File encoding: UTF-8
def main(num_of_iter, principal, rate):
    if num_of_iter == 0:
        return
    else:
        principal = principal + 0.1*principal
        num_of_iter -= 1
        print(principal)
        print(num_of_iter)

    main(num_of_iter, principal, rate)


main(30*3, 2000000, 0.1)
