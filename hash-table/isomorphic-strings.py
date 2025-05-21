class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_to_t = {}
        map_to_s = {}

        for c1, c2 in zip(s, t):
            if c1 in map_to_t:
                if map_to_t[c1] != c2:
                    return False
            else:
                map_to_t[c1] = c2

            if c2 in map_to_s:
                if map_to_s[c2] != c1:
                    return False
            else:
                map_to_s[c2] = c1

        return True
