class Solution:
    # time O(N), space O(1)
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ret = []

        for target in [tops[0], bottoms[0]]:
            counts = [0, 0]

            for t, b in zip(tops, bottoms):
                if t != target and b != target:
                    ret.append(-1)
                    break

                if t != target:
                    counts[1] += 1
                elif b != target:
                    counts[0] += 1

            else:
                ret.append(min(counts))

        return max(ret)
