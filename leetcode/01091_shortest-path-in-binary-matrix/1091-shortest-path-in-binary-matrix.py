class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        R, C = len(grid), len(grid[0])

        if grid[R - 1][C - 1] == 1:
            return -1

        offsets = (
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
        )

        visited = [[sys.maxsize] * C for _ in range(R)]

        nodes = deque([(0, 0, 1)])
        while nodes:
            r, c, steps = nodes.popleft()

            if not (0 <= r < R) or \
                    not (0 <= c < C):
                continue

            if grid[r][c] == 1:
                continue

            if steps >= visited[r][c]:
                continue

            visited[r][c] = steps

            for dr, dc in offsets:
                nodes.append((r + dr, c + dc, steps + 1))

        if visited[R - 1][C - 1] == sys.maxsize:
            return -1
        return visited[R - 1][C - 1]
