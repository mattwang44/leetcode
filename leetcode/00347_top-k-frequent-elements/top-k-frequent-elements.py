class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        heap = list(counter.values())
        min_val = min(heapq.nlargest(k, heap))

        ret = []
        for k, v in counter.items():
            if v >= min_val:
                ret.append(k)
        return ret
