i1 = '3141592653589793238462643383279502884197169399375105820974944592'
i2 = '2718281828459045235360287471352662497757247093699959574966967627'


def multiply_string(a, b):
    num_digits_a = len(a)
    num_digits_b = len(b)

    if num_digits_a == 1 or num_digits_b == 1:
        return str(int(a) * int(b))

    a1, a2 = a[:num_digits_a // 2], a[num_digits_a // 2:]
    b1, b2 = b[:num_digits_b // 2], b[num_digits_b // 2:]

    a1b1 = multiply_string(a1, b1)
    a1b2 = multiply_string(a1, b2)
    a2b1 = multiply_string(a2, b1)
    a2b2 = multiply_string(a2, b2)
    result = plus_string(
        plus_string(
            a1b1 + '0' * (len(b2) + len(a2)),
            a1b2 + '0' * len(a2)
        ),
        plus_string(
            a2b1 + '0' * len(b2),
            a2b2
        )
    )
    return result


def plus_string(a, b):
    result = ''
    t = 0

    diff = len(a) - len(b)
    if diff > 0:
        b = '0' * diff + b
    else:
        a = '0' * diff + a

    for i, j in list(zip(a, b))[::-1]:
        summation = int(i) + int(j)
        c = summation % 10
        result += str((c + t) % 10)

        t = summation // 10 + (c + t) // 10

    if t:
        return str(t) + result[::-1]
    return result[::-1]


if __name__ == "__main__":
    print(multiply_string(i1, i2))
    # 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
