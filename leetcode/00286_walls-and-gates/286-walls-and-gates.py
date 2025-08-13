class Solution:
    EMPTY = 2**31 - 1
    WALL = -1
    GATE = 0

    # time O(MN), space O(MN)
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        R, C = len(rooms), len(rooms[0])

        offsets = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        nodes = deque()
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == self.GATE:
                    nodes.append((r, c, 0))

        # begin from each gates, run BFS
        while nodes:
            r, c, step_count = nodes.popleft()

            for r_offset, c_offset in offsets:
                _r = r + r_offset
                _c = c + c_offset

                if (
                    not (0 <= _r < R)
                    or not (0 <= _c < C)
                    or rooms[_r][_c] != self.EMPTY
                ):
                    continue

                rooms[_r][_c] = step_count + 1
                nodes.append((_r, _c, step_count + 1))
