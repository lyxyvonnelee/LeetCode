class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = s[1:] + s[:-1]
        return ss.find(s) != -1