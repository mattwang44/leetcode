class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        nums.sort()
        curr = nums[0]
        step = 0
        accum = 0
        for n in nums[1:]:
            if n != curr:
                step += 1
                curr = n
            accum += step
        return accum
