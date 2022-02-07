class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        ret = [0] * l
        stack = []
        for idx, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                day = stack.pop()
                ret[day] = idx - day

            stack.append(idx)
        return ret
