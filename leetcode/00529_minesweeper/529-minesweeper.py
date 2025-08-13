class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        R, C = len(board), len(board[0])
        offsets = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        memo = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if board[r][c] not in ["M", "X"]:
                    continue
                for dr, dc in offsets:
                    _r = dr + r
                    _c = dc + c
                    if (0 <= _r < R) and (0 <= _c < C):
                        memo[_r][_c] += 1

        q = deque([click])
        while q:
            r, c = q.popleft()
            if board[r][c] != "E":
                continue
            if memo[r][c] > 0:
                board[r][c] = str(memo[r][c])
            else:
                board[r][c] = "B"
                for dr, dc in offsets:
                    _r = r + dr
                    _c = c + dc
                    if (0 <= _r < R) and (0 <= _c < C) and board[_r][_c] == "E":
                        q.append([_r, _c])
        return board
