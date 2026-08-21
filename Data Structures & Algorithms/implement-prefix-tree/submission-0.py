class PrefixTree:

    def __init__(self):
        self.letter_map = {}
        self.valid_end = False

    def insert(self, word: str) -> None:
        if not word:
            self.valid_end = True
            return
        if not word[0] in self.letter_map:
            self.letter_map[word[0]] = PrefixTree()
        self.letter_map[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return self.valid_end
        if not word[0] in self.letter_map:
            return False
        return self.letter_map[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        if not prefix[0] in self.letter_map:
            return False
        return self.letter_map[prefix[0]].startsWith(prefix[1:])
        