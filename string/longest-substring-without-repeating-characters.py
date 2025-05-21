class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        ch_dict = defaultdict(int)

        start = 0
        for i, ch in enumerate(s):
            if ch in ch_dict:
                if ch_dict[ch] >= start:
                    start = ch_dict[ch] + 1

            ch_dict[ch] = i
            max_length = max(max_length, i - start + 1)

        return max_length
