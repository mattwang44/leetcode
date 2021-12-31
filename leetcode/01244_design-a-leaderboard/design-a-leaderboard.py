import heapq


class Leaderboard:

    def __init__(self):
        self.board = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.board:
            self.board[playerId] = score
        else:
            self.board[playerId] += score

    def top(self, K: int) -> int:
        heap = list(self.board.values())
        heapq.heapify(heap)
        return sum(heapq.nlargest(K, heap))

    def reset(self, playerId: int) -> None:
        del self.board[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
