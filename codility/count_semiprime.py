# correctness: 100%
# performance: 20%

import math


def solution(N, P, Q):
    non_primes = {}
    for i in range(2, int(math.sqrt(N)) + 1):
        if i not in non_primes:
            for j in range(i**2, N, i):
                non_primes[j] = 1

    primes = set(range(2, N))
    primes -= set(non_primes.keys())
    primes = list(primes)

    semi_primes = []
    for idx, p in enumerate(primes):
        semi_primes.extend([prime * p for prime in primes[idx:]])
    semi_primes = [sp for sp in semi_primes if sp <= N]
    semi_primes.sort()

    M = len(P)
    ret = [0] * M
    PQ = zip(P, Q, range(M))
    for l, r, idx in PQ:
        for sp in semi_primes:
            if l <= sp <= r:
                ret[idx] += 1
    return ret
