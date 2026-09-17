class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        wordList.reverse()
        
        target = -1
        for i in range(len(wordList)):
            if endWord == wordList[i]:
                target = i
                break
        if target == -1:
            return 0

        n = len(wordList[0])
        conn = defaultdict(set)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                diff = 0
                for k in range(n):
                    if wordList[i][k] != wordList[j][k]:
                        diff += 1
                        if diff > 1:
                            break
                if diff == 1:
                    conn[i].add(j)
                    conn[j].add(i)

        q = deque()
        q.append((0, 0))
        visited = {}
        visited[0] = True
        while q:
            (c, d) = q.popleft()
            if c == target:
                return d + 1
            for n in conn[c]:
                if n not in visited:
                    visited[n] = True
                    q.append((n, d + 1))
        return 0