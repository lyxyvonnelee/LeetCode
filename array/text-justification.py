class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []
        result = []
        numOfLetters = 0

        for word in words:
            if numOfLetters + len(line) + len(word) > maxWidth:
                for i in range(maxWidth - numOfLetters):
                    line[i % (len(line) - 1 or 1)] += " "
                result.append("".join(line))
                line, numOfLetters = [], 0
            line.append(word)
            numOfLetters += len(word)

        result.append(" ".join(line).ljust(maxWidth))
        return result
