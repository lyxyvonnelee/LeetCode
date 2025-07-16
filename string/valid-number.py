class Solution:
    def isNumber(self, s: str) -> bool:
        if s == '' or s=='.' or s=='+' or s=='-':
            return False
        for i in range(len(s)):            
            if s[i].isalpha() and s[i]!='e' and s[i]!='E':
                return False
            if s[i] == '+' or s[i] == '-':
                if i==len(s)-1 or (i != 0 and s[i-1]!='e' and s[i-1]!='E'):
                    return False
                elif i==0 and not s[i+1].isdigit() and s[i+1] != '.':
                    return False               
                continue
            if s[i] == '.':
                if s.count('.')>1:
                    return False
                if (i == 0 and (not s[i+1].isdigit() or s.count('.')>1)) or (i==len(s)-1 and (not s[i-1].isdigit() or s.count('.')>1)):
                    return False
                elif not i==0 and not i==len(s)-1 and ((not s[i+1].isdigit() and s[i-1]!='+' and s[i-1]!='-' and s[i+1]!='e' and s[i+1]!='E') or (not s[i-1].isdigit() and s[i-1]!='+' and s[i-1]!='-' and s[i+1]!='e' and s[i+1]!='E')):
                    return False
                continue
            if s[i] == 'e' or s[i] == 'E':
                if s.count('e')>1 or s.count('E')>1:
                    return False
                if i == len(s)-1 or (not s[i+1].isdigit() and s[i+1] != '+' and s[i+1]!='-'):
                    return False
                elif '.' in s[i:]:
                    return False
                elif i == 0 or (not s[i-1].isdigit() and s[i-1]!='.'):
                    return False
        
        return True