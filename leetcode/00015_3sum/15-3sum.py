class Solution:
    def twoSum(self, nums, target):
        memo = {}
        ret = []
        for num in nums:
            if target - num in memo:
                result = [target - num, num]
                if result not in ret:
                    ret.append(result)
            else:
                memo[num] = 1
        return ret

    # time O(N^2)
    # space O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums

        nums.sort()
        ret = []
        prev = None
        for idx, num in enumerate(nums):
            if num == prev:
                continue
            for result in self.twoSum(nums[idx + 1 :], -num):
                ret.append([num] + result)
            prev = num
        return ret
