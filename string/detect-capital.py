class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        a = word.capitalize()
        b = word.upper()
        c = word.lower()
        if word == a or word == b or word == c:
            return True
        else:
            return False
        