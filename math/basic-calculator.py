class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        sign = 1
        i = 0

        while i < len(s):
            char = s[i]
            if char.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                result += sign * num
                i -= 1
            elif char == "+":
                sign = 1
            elif char == "-":
                sign = -1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                result *= stack.pop()
                result += stack.pop()

            i += 1

        return result
