import sys


def solution(A):
    if not A:
        return 1

    fib = [0, 1]
    while fib[-1] <= len(A):
        fib.append(fib[-1] + fib[-2])

    # end
    A.append(1)

    d = {}
    for idx, n in enumerate(A):
        if n == 0:
            continue
        for step in fib[2:]:
            if idx - step < -1:
                break
            if idx - step == -1:
                d[idx] = 1
                break
            if idx - step in d:
                d[idx] = min(d[idx - step] + 1, d.get(idx, sys.maxsize))

    return d.get(idx, -1)
