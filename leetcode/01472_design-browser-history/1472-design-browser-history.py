class BrowserHistory:
    def __init__(self, homepage: str):
        self.h = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.i += 1
        self.h = self.h[: self.i] + [url]

    def back(self, steps: int) -> str:
        self.i = max(0, self.i - steps)
        return self.h[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(len(self.h) - 1, self.i + steps)
        return self.h[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
