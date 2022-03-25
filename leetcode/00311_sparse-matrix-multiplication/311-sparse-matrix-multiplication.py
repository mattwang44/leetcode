class Solution:
    # time O(mkn), space O(1)
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        ret = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                for i in range(k):
                    if mat1[r][i] and mat2[i][c]:
                        ret[r][c] += mat2[i][c] * mat1[r][i]
        return ret
