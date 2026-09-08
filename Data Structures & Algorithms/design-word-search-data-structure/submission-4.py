class Node:
    def __init__(self):
        self.isWord = False
        self.children = [None] * 26;


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c)-ord('a')
            if cur.children[i] is None:
                cur.children[i] = Node()
            cur = cur.children[i]
        cur.isWord = True

    def searchWithNode(self, word, node):
        if node is None:
            return False
        elif (len(word) == 0):
            print("done")
            return node.isWord
        else:
            c = word[0]
            if (c == "."):
                # print([self.searchWithNode(word[1:], node.children[i]) for i in range(26)])
                return any([self.searchWithNode(word[1:], node.children[i])for i in range(26)] );
            else:
                i = ord(c)-ord('a')
                return self.searchWithNode(word[1:], node.children[i])

    def search(self, word: str) -> bool:
        return self.searchWithNode(word, self.root)

        
