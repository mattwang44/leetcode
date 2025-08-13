class Solution:
    # time O(NlogN), space O(1)
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        length = len(costs)
        costs.sort(key=lambda x: x[1] - x[0])
        return sum(c[1] for c in costs[: length // 2]) + sum(
            c[0] for c in costs[length // 2 :]
        )
