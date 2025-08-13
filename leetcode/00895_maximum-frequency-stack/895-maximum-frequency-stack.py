from collections import Counter, defaultdict

# time O(1) for push & pop, space O(N)


class FreqStack:
    def __init__(self):
        self.freq = Counter()
        self.groups = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.max_freq = max(self.max_freq, self.freq[val])
        self.groups[self.freq[val]].append(val)

    def pop(self) -> int:
        val = self.groups[self.max_freq].pop()
        self.freq[val] -= 1

        if len(self.groups[self.max_freq]) == 0:
            self.max_freq -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
