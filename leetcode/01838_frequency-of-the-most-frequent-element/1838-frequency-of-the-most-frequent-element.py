class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        ops = 0
        l = 0
        for r, num in enumerate(nums):
            k -= (r - l) * (num - nums[r - 1])
            while k < 0:
                k += (num - nums[l])
                l += 1
            ops = max(ops, r - l + 1)
        return ops
