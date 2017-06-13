class TrieNode(object):
    def __init__(self):
        self.leaves = {}
        self.is_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.leaves:
                node.leaves[w] = TrieNode()
            node = node.leaves[w]
        node.is_word = True

    def search(self, word):
        node = self.root
        for w in word:
            if w not in node.leaves:
                return False
            node = node.leaves[w]
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for p in prefix:
            if p not in node.leaves:
                return False
            node = node.leaves[p]
        return True
