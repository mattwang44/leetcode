class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        dirs = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
        ]
        dir_idx = 0
        ret = [0] * (R * C)
        m = n = 0
        for i in range(R * C):
            ret[i] = matrix[m][n]
            matrix[m][n] = None

            _m = m + dirs[dir_idx][0]
            _n = n + dirs[dir_idx][1]
            if not 0 <= _m < R or \
                    not 0 <= _n < C or \
                    matrix[_m][_n] is None:
                dir_idx = (dir_idx + 1) % 4

            m += dirs[dir_idx][0]
            n += dirs[dir_idx][1]
        return ret
