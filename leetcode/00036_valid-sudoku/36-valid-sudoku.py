class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for b in board:
            print(b)

        def validate(l: List) -> bool:
            numbers = []
            if not all(e == "." or numbers.append(e) or 1 <= int(e) <= 9 for e in l):
                return False
            if len(numbers) != len(set(numbers)):
                return False
            if len(numbers) < 9:
                return True
            if sum(l) == 45:
                return True
            return False

        for i in range(9):
            if not validate(board[i]):
                return False
            if not validate([board[j][i] for j in range(9)]):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not validate(
                    sum(
                        [
                            [board[l][k] for k in range(j, j + 3)]
                            for l in range(i, i + 3)
                        ],
                        [],
                    )
                ):
                    return False

        return True
