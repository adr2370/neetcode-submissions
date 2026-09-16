class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        conn = defaultdict(set)
        connLen = defaultdict(int)
        for s, e in edges:
            conn[s].add(e)
            connLen[s] += 1
            conn[e].add(s)
            connLen[e] += 1

        q = deque()
        for s, i in connLen.items():
            if i == 1:
                q.append(s)
        while q:
            n = q.popleft()
            for c in conn[n]:
                connLen[c] -= 1
                if connLen[c] == 1:
                    q.append(c)
        
        for i in range(len(edges) - 1, -1, -1):
            s, e = edges[i]
            if connLen[s] > 1 and connLen[e] > 1:
                return [s, e]
        return []