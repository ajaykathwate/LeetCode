class Solution:
    @lru_cache(None)
    def detectCapitalUse(self, word: str) -> bool:
        if (word[0].isupper() and word[1:].islower()) or word.isupper() or word.islower():
            return True
        else:
            return False