class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        accs = [0] * (len(nums) + 1)
        for idx, num in enumerate(nums):
            accs[idx + 1] = accs[idx] + num

        min_dist = sys.maxsize
        q = deque()
        for idx, acc in enumerate(accs):
            while q and acc <= accs[q[-1]]:
                q.pop()

            while q and (acc - accs[q[0]]) >= k:
                min_dist = min(min_dist, idx - q[0])
                q.popleft()

            q.append(idx)

        return min_dist if min_dist < sys.maxsize else -1
