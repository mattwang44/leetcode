class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2
            total, res = 0, 1
            for weight in weights:
                if total + weight > mid:
                    res += 1
                    total = weight
                else:
                    total += weight

            if res <= days:
                r = mid
            else:
                l = mid + 1

        return l
