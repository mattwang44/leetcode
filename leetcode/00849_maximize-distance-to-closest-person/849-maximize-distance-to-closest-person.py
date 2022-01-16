class Solution:
    # time O(N), space O(N)
    def maxDistToClosest(self, seats: List[int]) -> int:
        length = len(seats)
        memo = {}

        last_one_idx = None
        for idx in range(0, length):
            if seats[idx] == 1:
                last_one_idx = idx
            elif seats[idx] == 0 and last_one_idx is not None:
                memo[idx] = min(
                    idx - last_one_idx,
                    memo.get(idx, sys.maxsize),
                )

        last_one_idx = None
        for idx in range(length - 1, -1, -1):
            if seats[idx] == 1:
                last_one_idx = idx
            elif seats[idx] == 0 and last_one_idx is not None:
                memo[idx] = min(
                    last_one_idx - idx,
                    memo.get(idx, sys.maxsize),
                )

        return max(memo.values())
