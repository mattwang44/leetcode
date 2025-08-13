class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1, y1)  # bottom-left
        self.p2 = Point(x2, y2)  # top-right

    @property
    def area(self):
        return abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y)

    def get_overlapped_rec(self, rec):
        if (
            rec.p2.x < self.p1.x
            and rec.p1.x < self.p1.x
            or rec.p2.x > self.p2.x
            and rec.p1.x > self.p2.x
            or rec.p2.y < self.p1.y
            and rec.p1.y < self.p1.y
            or rec.p2.y > self.p2.y
            and rec.p1.y > self.p2.y
        ):
            return Rectangle(0, 0, 0, 0)

        return Rectangle(
            max(rec.p1.x, self.p1.x),
            max(rec.p1.y, self.p1.y),
            min(rec.p2.x, self.p2.x),
            min(rec.p2.y, self.p2.y),
        )


class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        rec1 = Rectangle(ax1, ay1, ax2, ay2)
        rec2 = Rectangle(bx1, by1, bx2, by2)
        return rec1.area + rec2.area - rec1.get_overlapped_rec(rec2).area
