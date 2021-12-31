class Solution:
    # time O(NlogN), space O(N)
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1, 3, 2, 4 -> 1, 3, 4, 2 (2 is pivot)
        # 1, 1, 1, 5 -> 1, 1, 5, 1 (the 3rd 1 is pivot)
        # 0, 1, 3, 2 -> 0, 2, 1, 3 (1 is pivot)
        # 1, 4, 3, 2 -> 2, 1, 3, 4 (1 is pivot)

        if len(nums) <= 1:
            return

        curr = nums[-1]
        for i in range(len(nums) - 2, -2, -1):
            if i == -1:
                break
            if nums[i] >= curr:
                curr = nums[i]
                continue
            elif nums[i] < curr:  # pivot at index i
                break

        # return sorted nums if nums is a descending array
        if i == -1:
            nums.sort()
            return

        # find pivot element and the next lexicographical number
        pivot = nums[i]
        idx_to_swap = None
        for idx, n in enumerate(nums[i+1:]):
            if n > pivot:
                idx_to_swap = i + idx + 1
                continue
            break

        nums[i], nums[idx_to_swap] = nums[idx_to_swap], nums[i]
        nums[i+1:] = sorted(nums[i+1:])
