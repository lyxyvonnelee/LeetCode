class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available_letters = Counter(magazine)

        for char in ransomNote:
            if char not in available_letters:
                return False

            available_letters[char] -= 1
            if available_letters[char] < 0:
                return False

        return True
