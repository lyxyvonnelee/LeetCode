class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = list()
        for i in s:
            if result and i == result[-1]:
                result.pop()
            else:
                result.append(i)
        return ''.join(result)