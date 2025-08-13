class Solution:
    # time O(N), space O(1)
    def to_xy(self, deg):
        return round(math.cos(deg), 4), round(math.sin(deg), 4)

    def isRobotBounded(self, instructions: str) -> bool:
        deg = math.pi / 2
        start = curr = (0, 0)

        for char in instructions:
            if char == "G":
                x, y = self.to_xy(deg)
                curr = (curr[0] + x, curr[1] + y)
            elif char == "L":
                deg += math.pi / 2
            elif char == "R":
                deg -= math.pi / 2

        if start == curr:
            return True

        deg = deg % (math.pi * 2)
        return round(deg - math.pi / 2, 4)
