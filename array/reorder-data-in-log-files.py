class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        letter = []
        for log in logs:
            tmp = log.split()
            if tmp[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
        letter.sort(key = lambda x: (x.split()[1:], x[0]))          
            
        logs = letter.extend(digit)
        return letter