class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def traversal(r, c):
            if not (0 <= r < R) or not (0 <= c < C) or grid[r][c] != 1:
                return 0

            grid[r][c] = 0

            return (
                1
                + traversal(r, c + 1)
                + traversal(r, c - 1)
                + traversal(r + 1, c)
                + traversal(r - 1, c)
            )

        max_area = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    max_area = max(max_area, traversal(i, j))
        return max_area
