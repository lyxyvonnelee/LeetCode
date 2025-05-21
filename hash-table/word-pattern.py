class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False

        map_to_s = {}
        map_to_p = {}

        for c, word in zip(pattern, s.split()):
            if c in map_to_s:
                if map_to_s[c] != word:
                    return False
            else:
                map_to_s[c] = word

            if word in map_to_p:
                if map_to_p[word] != c:
                    return False
            else:
                map_to_p[word] = c

        return True
