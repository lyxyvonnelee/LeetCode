class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = Counter(s)

        for char in t:
            if char not in t:
                return False
            s_count[char] -= 1
            if s_count[char] < 0:
                return False

        return True
