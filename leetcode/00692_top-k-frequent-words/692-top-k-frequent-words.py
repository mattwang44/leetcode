import collections
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        ret = heapq.nsmallest(k, counter.keys(), key=lambda k: (-counter[k], k))
        return ret
