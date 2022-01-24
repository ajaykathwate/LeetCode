class Solution:
    def capitalizeTitle(self, title: str) -> str:
        arr = title.split(" ")
        lst = []
        for i in arr:
            if len(i) >= 3:
                ttl = i[0].upper() + i[1:].lower()
                lst.append(ttl)
            else:
                w = i.lower()
                lst.append(w)
        return " ".join(lst)