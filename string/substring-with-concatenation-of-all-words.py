class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        word_length = len(words[0])
        numOfWords = len(words)
        total_length = numOfWords * word_length
        word_count = Counter(words)

        for offset in range(word_length):
            left = offset
            seen = Counter()
            word_found = 0

            for right in range(offset, len(s) - word_length + 1, word_length):
                word = s[right : right + word_length]
                if word in word_count:
                    seen[word] += 1
                    word_found += 1

                    while seen[word] > word_count[word]:
                        left_word = s[left : left + word_length]
                        seen[left_word] -= 1
                        left += word_length
                        word_found -= 1

                    if word_found == numOfWords:
                        result.append(left)

                else:
                    seen.clear()
                    word_found = 0
                    left = right + word_length

        return result
