class Solution:
    @lru_cache(None)
    def toLowerCase(self, s: str) -> str:
        return s.lower()