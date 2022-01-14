class Solution:
    def twoEggDrop(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1
            n -= count
        return count
