class Solution:
    # time O(N), space O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_idx = []
        non_zeros = []
        for idx, n in enumerate(nums):
            if n == 0:
                zero_idx.append(idx)
            else:
                non_zeros.append(n)

        zero_count = len(zero_idx)

        # not any zero
        if zero_count == 0:
            product = reduce(lambda x, y: x * y, nums)
            return [product // i for i in nums]

        # only one zero
        elif zero_count == 1:
            product = reduce(lambda x, y: x * y, non_zeros)
            ret = [0] * len(nums)
            ret[zero_idx[0]] = product
            return ret

        # more than 2 zero
        return [0] * len(nums)
