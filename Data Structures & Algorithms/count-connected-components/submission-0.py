class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        conn = defaultdict(set)
        for s, e in edges:
            conn[s].add(e)
            conn[e].add(s)
        
        q = deque()
        visited = {}
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                q.append(i)
                visited[i] = True
                while q:
                    n = q.popleft()
                    for e in conn[n]:
                        if e not in visited:
                            q.append(e)
                            visited[e] = True
        return count