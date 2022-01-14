class Solution:
    # time O(NlogN), space O(N)
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        merged = points[0]
        count = 1
        for point in points[1::]:
            if point[0] > merged[1]:
                merged = point
                count += 1
            else:
                merged = [point[0], min(point[1], merged[1])]
        return count
