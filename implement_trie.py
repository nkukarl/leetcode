class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.is_word = True

    def search(self, word):
        if '' == word:
            return False
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.is_word

    def starts_with(self, prefix):
        if '' == prefix:
            return False
        node = self.root
        for p in prefix:
            if p not in node.children:
                return False
            node = node.children[p]
        return True
