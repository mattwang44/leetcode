from collections import defaultdict


class WordDictionary:

    def __init__(self):
        self.trie = defaultdict(lambda x: defaultdict)

    def addWord(self, word: str) -> None:
        curr = self.trie
        for char in word:
            curr = curr.setdefault(char, {})
        curr['$'] = True

    def search_helper(self, word: str, node: dict) -> bool:
        for idx, char in enumerate(word):
            if char in node:
                node = node[char]
            elif char == '.':
                for key in node:
                    if key != '$' and self.search_helper(word[idx+1:], node[key]):
                        return True
                return False
            else:
                return False

        return '$' in node

    def search(self, word: str) -> bool:
        return self.search_helper(word, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
