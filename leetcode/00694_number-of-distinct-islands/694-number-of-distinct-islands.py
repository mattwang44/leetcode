class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        unique_encoded = set()

        offsets = (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        )

        def bfs(start_r, start_c):
            nodes = deque([(start_r, start_c)])
            encoded = list()

            while nodes:
                r, c = nodes.popleft()
                if not (0 <= r < R) or not (0 <= c < C) or grid[r][c] == 0:
                    continue

                encoded.append((r - start_r, c - start_c))
                grid[r][c] = 0

                for dr, dc in offsets:
                    nodes.append((r + dr, c + dc))

            return ",".join(str(e) for e in encoded)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue

                encoded = bfs(r, c)
                unique_encoded.add(encoded)

        return len(unique_encoded)
