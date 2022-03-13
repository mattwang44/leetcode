class Solution:
    # time O(N^2), space O(N)
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l = len(nums)
        count = 0

        counter = Counter()
        start_idx = 0
        for idx, num in enumerate(nums):
            counter[num] += 1
            if len(counter) < k:
                continue

            if len(counter) == k:
                count += 1

            while len(counter) > k:
                counter[nums[start_idx]] -= 1
                if counter[nums[start_idx]] == 0:
                    del counter[nums[start_idx]]
                if len(counter) == k:
                    count += 1
                start_idx += 1

            temp = counter.copy()
            for i in range(start_idx, idx - k + 1):
                temp[nums[i]] -= 1
                if temp[nums[i]] == 0:
                    del temp[nums[i]]
                if len(temp) == k:
                    count += 1
                elif len(temp) < k:
                    break

        return count

    # PEEKED ANSWER, time O(N), space O(N)
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    def atMostK(self, nums, k):
        start_idx = 0
        counter = defaultdict(int)
        count = 0
        for end_idx, num in enumerate(nums):
            counter[num] += 1
            while len(counter) > k:
                counter[nums[start_idx]] -= 1
                if counter[nums[start_idx]] == 0:
                    del counter[nums[start_idx]]
                start_idx += 1

            count += end_idx - start_idx + 1
        return count
