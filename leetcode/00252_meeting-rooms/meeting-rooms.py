class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for idx, interval in enumerate(intervals[:-1]):
            if interval[1] > intervals[idx + 1][0]:
                return False
        return True