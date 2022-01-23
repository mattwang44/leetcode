class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mi = lo + (hi - lo) // 2
                if nums[mi] >= target:
                    hi = mi - 1
                else:
                    lo = mi + 1
            return lo

        def findRight():
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mi = lo + (hi - lo) // 2
                if nums[mi] <= target:
                    lo = mi + 1
                else:
                    hi = mi - 1
            return hi

        l, r = findLeft(), findRight()
        return [l, r] if l <= r else [-1, -1]
