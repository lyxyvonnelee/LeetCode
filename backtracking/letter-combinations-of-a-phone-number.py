class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        result = []
        digit_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                     '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        def backtrack(st, path):
            if len(path) == len(digits):
                result.append(path)
                return
            
            possible_letters = digit_map[digits[st]]
            for l in possible_letters:
                backtrack(st+1, path+l)

        backtrack(0, '')
        return result