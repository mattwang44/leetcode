class Solution:
    # Try applying binary search next time
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        pass

    # BRUTE FORCE
    # time O(N^3), space O(1)

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) <= 2:
            return 0

        nums.sort()
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] < target:
                        count += 1
                    else:
                        break
        return count
