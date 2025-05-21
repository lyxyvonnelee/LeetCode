class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for i, ch in enumerate(word):
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end_of_word = True

    def search(self, word):
        cur = self.root
        for i, ch in enumerate(word):
            if ch not in cur.children:
                return word
            cur = cur.children[ch]
            if cur.is_end_of_word == True:
                return word[:i+1]
            
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dct = Trie()
        for root in dictionary:
            dct.insert(root)

        return " ".join(dct.search(word) for word in sentence.split())