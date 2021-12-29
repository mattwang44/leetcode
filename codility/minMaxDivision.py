def is_valid(A, size, K):
    curr = 0
    count = 0
    for n in A:
        if curr + n > size:
            curr = n
            count += 1
        else:
            curr += n
    if curr > 0:
        count += 1
    return count <= K


def solution(K, M, A):
    l = max(A)
    r = sum(A)
    while l < r:
        mid = l + (r - l) // 2
        if is_valid(A, mid, K):
            r = mid
        else:
            l = mid + 1
    return l
