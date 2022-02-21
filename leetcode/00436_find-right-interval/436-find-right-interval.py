import bisect


class Solution:
    # time O(NlogN), space O(N)
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        memo = {}
        for idx, (start, _) in enumerate(intervals):
            memo[start] = idx

        keys = [e[0] for e in intervals]
        keys.sort()

        ret = [0] * len(intervals)
        for idx, (_, end) in enumerate(intervals):
            key_idx = bisect.bisect_left(keys, end)
            if key_idx == len(keys):
                ret[idx] = -1
            else:
                ret[idx] = memo[keys[key_idx]]

        return ret
