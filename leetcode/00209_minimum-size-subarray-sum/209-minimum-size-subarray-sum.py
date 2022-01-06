class Solution:
    # time O(N), space O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = 0
        min_count = sys.maxsize
        _sum = 0
        ptr = 0
        for n in nums:
            _sum += n
            count += 1

            while _sum >= target:
                min_count = min(min_count, count)
                _sum -= nums[ptr]
                ptr += 1
                count -= 1

        return min_count if min_count != sys.maxsize else 0
