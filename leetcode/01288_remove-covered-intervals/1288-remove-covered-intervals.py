class Solution:
    # time O(NlogN), space O(N)
    # Try not to create additional space next time
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1] - x[0])

        def compare_intervals(i1, i2):
            l1, r1 = i1
            l2, r2 = i2

            if l1 <= l2 and r1 >= r2:
                return True, i1

            if l1 >= l2 and r1 <= r2:
                return True, i2

            return False, None

        ret = []
        for interval in intervals[::-1]:
            if not ret:
                ret.append(interval)
                continue

            any_covered = False
            for idx, target_interval in enumerate(ret):
                is_covered, result_interval = compare_intervals(
                    target_interval, interval
                )
                if is_covered:
                    ret[idx] = result_interval
                    any_covered = True
                    break

            if not any_covered:
                ret.append(interval)

        return len(ret)
