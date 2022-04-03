class Solution:
    # time O(N), space O(1)
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l <= 1:
            return

        # find the first decreasing number
        for idx in range(l - 2, -1, -1):
            if nums[idx+1] > nums[idx]:
                break
        else:
            # if not exist, nums in reverse order is the answer
            nums.reverse()
            return

        # find the number just larger than nums[idx]
        for i in range(idx+1, l):
            if nums[i] <= nums[idx]:
                i -= 1
                break
        else:
            i = l - 1

        # swap the two above indices, and revese the part after the index idx
        nums[idx], nums[i] = nums[i], nums[idx]
        nums[idx+1:] = nums[idx+1:][::-1]
        return
