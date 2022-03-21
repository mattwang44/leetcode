class Solution:
    # time O(N), space O(1)
    def partitionLabels(self, s: str) -> List[int]:
        memo = {char: idx for idx, char in enumerate(s)}

        partitions = []
        prev = idx = 0

        while idx < len(s):
            curr_max = memo[s[idx]]

            while idx <= curr_max:
                curr_max = max(curr_max, memo[s[idx]])
                idx += 1

            partitions.append(idx - prev)
            prev = idx

        return partitions
