class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        t_count = Counter(t)
        required = len(t_count)

        cur_window = defaultdict(int)
        form = 0
        l, r = 0, 0
        min_len = float("inf")
        min_window = (0, 0)

        while r < len(s):
            c = s[r]
            cur_window[c] += 1

            if c in t_count and cur_window[c] == t_count[c]:
                form += 1

            while l <= r and form == required:
                length = r - l + 1
                if length < min_len:
                    min_len = length
                    min_window = (l, r)

                lc = s[l]
                cur_window[lc] -= 1
                if lc in t_count and cur_window[lc] < t_count[lc]:
                    form -= 1

                l += 1

            r += 1

        l, r = min_window
        return s[l:r + 1] if min_len != float("inf") else ""
