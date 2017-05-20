class Trie(object):
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary(object):
    def __init__(self):
        self.root = Trie()

    def add_word(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Trie()
            node = node.children[w]
        node.is_word = True

    def search(self, word):
        node = self.root
        return self._search(word, node)

    def _search(self, word, node):
        if '' == word:
            return node.is_word

        if '.' == word[0]:
            for char in node.children:
                if self._search(word[1:], node.children[char]):
                    return True
            return False
        if word[0] in node.children:
            return self._search(word[1:], node.children[word[0]])
        return False
