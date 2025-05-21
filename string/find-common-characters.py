class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        tmp = Counter(words[0])
        for i in range(1, len(words)):
            tmp = tmp & Counter(words[i])
        print(tmp)
        res = []
        for c in tmp:
            for i in range(tmp[c]):
                res.append(c)
        return res
