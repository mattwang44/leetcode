class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 0, max(piles)
        while hi > lo:
            mi = lo + (hi - lo) // 2
            if not mi:
                break
            if sum(int((p - 1) / mi) + 1 for p in piles) <= h:
                hi = mi
            else:
                lo = mi + 1

        return hi
