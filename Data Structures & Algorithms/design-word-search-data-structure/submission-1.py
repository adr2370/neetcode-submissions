class WordDictionary:

    def __init__(self):
        self.m = {}
        self.end = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if not c in curr.m:
                curr.m[c] = WordDictionary()
            curr = curr.m[c]
        curr.end = True

    def search(self, word: str) -> bool:
        options = [self]
        next_options = []
        for c in word:
            for curr in options:
                if c == ".":
                    for n in curr.m.values():
                        next_options.append(n)
                elif c in curr.m:
                    next_options.append(curr.m[c])
            options = next_options
            next_options = []
        for o in options:
            if o.end == True:
                return True
        return False
