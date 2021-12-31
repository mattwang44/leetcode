class Solution:
    # value as hash key and mark as 1
    # time O(4N), space O(1)
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)

        if 1 not in nums:
            return 1

        for idx, num in enumerate(nums):
            if num > length or num <= 0:
                nums[idx] = 1

        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])

        for idx, num in enumerate(nums):
            if num > 0:
                return idx + 1
        return length + 1

    # value as hash key and recursively mark as None
    # time O(2N), space O(1)

    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)

        def mark(num):
            if num is None or num > length or num <= 0:
                return

            # handle the value pointed by the current value
            # after current marking is done
            temp = nums[num - 1]
            nums[num - 1] = None
            mark(temp)

        for num in nums:
            mark(num)

        for idx, num in enumerate(nums):
            if num is not None:
                return idx + 1
        return length + 1
