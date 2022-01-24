class Solution:
    @lru_cache(None)
    def capitalizeTitle(self, title: str) -> str:return " ".join([(i[0].upper() + i[1:].lower())  if len(i) >= 3 else i.lower() for i in title.split(" ")])