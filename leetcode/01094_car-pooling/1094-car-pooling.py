class Solution:
    # time O(NlogN), space O(N)
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        memo = {}
        for trip in trips:
            num_passengers, _from, _to = trip
            memo[_from] = memo.get(_from, 0) + num_passengers
            memo[_to] = memo.get(_to, 0) - num_passengers

        memo = sorted(memo.items(), key=lambda kv: abs(kv[0]))
        curr_passengers = 0
        for _, passaenger_diff in memo:
            curr_passengers += passaenger_diff
            if curr_passengers > capacity:
                return False
        return True
