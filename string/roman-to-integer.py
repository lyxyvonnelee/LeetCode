class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev = 0
        for char in reversed(s):
            cur = roman_values[char]
            if cur < prev:
                result -= cur
            else:
                result += cur
            prev = cur

        return result
