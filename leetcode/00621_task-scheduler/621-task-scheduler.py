from collections import Counter


class Solution:
    # TLE, time O(N), space O(1) (26 alphabet)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        last_exec_idx = {task: None for task in counter}
        ops_count = 0

        while counter:
            for task, count in counter.most_common():
                if counter[task] == 0:
                    continue

                if (
                    last_exec_idx[task] is not None
                    and ops_count - last_exec_idx[task] <= n
                ):
                    continue

                last_exec_idx[task] = ops_count
                counter[task] -= 1
                if counter[task] == 0:
                    del counter[task]
                break

            ops_count += 1

        return ops_count

    # time O(N), space O(1)

    def leastInterval(self, tasks: List[str], n: int) -> int:
        total = len(tasks)
        if n == 0:
            return total

        counter = Counter(tasks)
        count_heaviest_task = counter.most_common()[0][1]
        num_tasks_max_count = sum(v == count_heaviest_task for v in counter.values())

        return max(
            (count_heaviest_task - 1) * (n + 1) + num_tasks_max_count,
            total,
        )
