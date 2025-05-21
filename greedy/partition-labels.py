class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastAppearance = {}
        for i, ch in enumerate(s):
            lastAppearance[ch] = i
        
        res, st, end = [], 0, 0
        for i, ch in enumerate(s):
            end = max(end, lastAppearance[ch])

            if end == i:
                res.append(end - st + 1)
                st = i+1
        
        return res
