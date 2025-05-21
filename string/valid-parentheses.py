class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            
        dct = {")": "(", "}": "{", "]": "["}
        tmp = []

        for char in s:
            if char in "([{":
                tmp.append(char)
            else:
                paired = dct[char]
                if not tmp or paired != tmp.pop():
                    return False

        return True if not tmp else False
