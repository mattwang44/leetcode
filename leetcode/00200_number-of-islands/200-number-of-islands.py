class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]
        count = 0

        def dfs(r, c):
            if not 0 <= r < R or not 0 <= c < C or grid[r][c] is not "1":
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "0":
                    continue
                dfs(r, c)
                count += 1

        return count
