class Solution:
    # time O(N), space O(1)
    def longestOnes(self, nums: List[int], k: int) -> int:
        start_idx = 0
        max_length = 0

        for end_idx, num in enumerate(nums):
            if num == 0:
                k -= 1

            while k < 0:
                if nums[start_idx] == 0:
                    k += 1
                start_idx += 1

            max_length = max(max_length, end_idx - start_idx + 1)

        return max_length
