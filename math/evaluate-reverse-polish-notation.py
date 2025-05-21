class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for num in tokens:
            if num not in "+-*/":
                nums.append(num)
            else:
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(str(int(eval(num1 + num + num2))))

        return int(nums[-1])
