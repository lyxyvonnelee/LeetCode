class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        for num in nums:
            if num - 1 not in nums:
                cur_interval = str(num)
                start = num

                while num + 1 in nums:
                    num += 1

                if num != start:
                    cur_interval += "->" + str(num)
                result.append(cur_interval)

        return result
