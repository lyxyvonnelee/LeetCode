class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        lst = reversed(s.split())
        return " ".join(lst)
