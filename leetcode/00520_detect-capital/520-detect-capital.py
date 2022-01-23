class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper_count = sum(char.isupper() for char in word)

        if upper_count == len(word):
            return True
        if upper_count == 0:
            return True
        if upper_count == 1 and word[0].isupper():
            return True
        return False
