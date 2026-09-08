class node:
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = node()
            curr = curr.children[c]
        curr.word = True

    def search_empty(self, word: str, curr_node) -> bool:
        curr = curr_node
        for i in range(len(word)):
            c = word[i]
            if c == ".":
                return any([self.search_empty(word[i+1:], curr.children[c]) for c in curr.children])
            else:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
        return curr.word

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            if c == ".":
                return any([self.search_empty(word[i+1:], curr.children[c]) for c in curr.children])
            else:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
        return curr.word
