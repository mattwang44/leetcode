class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        memo = {}
        for _from, _to in intervals:
            memo[_from] = memo.get(_from, 0) + 1
            memo[_to] = memo.get(_to, 0) - 1

        memo = sorted(memo.items(), key=lambda kv: kv[0])
        curr_room = 0
        max_room = 0
        for _, diff in memo:
            curr_room += diff
            max_room = max(max_room, curr_room)
        return max_room
