class TrieNode(object):
    def __init__(self):
        self.leaves = {}
        self.is_word = False


class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for w in word:
            if w not in node.leaves:
                node.leaves[w] = TrieNode()
            node = node.leaves[w]
        node.is_word = True

    def search(self, word):
        node = self.root
        return self._search(word, node)

    def _search(self, word, node):
        if '' == word:
            return node.is_word
        w = word[0]
        if '.' == w:
            for char in node.leaves:
                if self._search(word[1:], node.leaves[char]):
                    return True
            return False
        if w in node.leaves:
            return self._search(word[1:], node.leaves[w])
        return False
