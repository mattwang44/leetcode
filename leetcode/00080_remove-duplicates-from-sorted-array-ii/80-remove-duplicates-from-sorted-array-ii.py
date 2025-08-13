class Solution:
    # time O(N), space O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        # init with the first element in nums
        curr_num = nums[0]
        idx_lag = 0
        count = 1

        for idx, num in enumerate(nums):
            # skip the first iteration
            if idx == 0:
                continue

            # increment count if the value is same as the last one,
            # or reset if it's a new value
            if num == curr_num:
                count += 1
            else:
                count = 1
                curr_num = num

            # if the occurrence is larger than 2, increment the index lag
            if count > 2:
                idx_lag += 1

            # move the curr value
            nums[idx - idx_lag] = num

        return len(nums) - idx_lag
