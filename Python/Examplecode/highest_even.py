numbers = [44, 10, 12, 13, 25, 3, 87, 45, 22]


def highest_even(num):
    even_num = []
    # even_num = (x for x in num if x % 2 == 0)

    for x in num:
        if x % 2 == 0:
            even_num.append(x)

    return max(even_num)


print(highest_even(numbers))
