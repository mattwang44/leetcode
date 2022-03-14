from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # construct memo
        l = len(beginWord)
        memo = defaultdict(list)
        for word in wordList:
            for i in range(l):
                residual = word[:i] + '_' + word[i+1:]
                memo[residual].append(word[i])

        # bfs
        seen = set()
        stack = deque([(beginWord, 1)])
        while stack:
            word, count = stack.popleft()
            if word == endWord:
                return count

            if word in seen:
                continue
            seen.add(word)

            for i, char in enumerate(word):
                residual = word[:i] + '_' + word[i+1:]
                for e in memo[residual]:
                    stack.append((word[:i] + e + word[i+1:], count + 1))

        return 0
