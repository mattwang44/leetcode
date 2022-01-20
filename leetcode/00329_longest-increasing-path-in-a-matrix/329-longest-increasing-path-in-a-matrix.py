class Solution:
    # time O(MN), space O(MN)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])

        memo = [[None] * C for _ in range(R)]

        offsets = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        def dfs(r, c):
            if memo[r][c] is not None:
                return memo[r][c]

            dist = 1
            for offset in offsets:
                dr, dc = offset
                if not (0 <= r+dr < R) or \
                   not (0 <= c+dc < C) or \
                   matrix[r][c] >= matrix[r+dr][c+dc]:
                    continue
                dist = max(dist, dfs(r+dr, c+dc) + 1)
            memo[r][c] = dist
            return dist

        longest_path = 0
        for r in range(R):
            for c in range(C):
                longest_path = max(longest_path, dfs(r, c))
        return longest_path
