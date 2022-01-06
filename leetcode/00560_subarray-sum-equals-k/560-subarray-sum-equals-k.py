class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = {}
        accs = [0] * (len(nums) + 1)
        for idx, num in enumerate(nums):
            accs[idx + 1] = accs[idx] + num

        counter = collections.Counter(accs)

        count = 0
        for acc in accs:
            counter[acc] -= 1
            count += counter.get(k + acc, 0)
        return count
