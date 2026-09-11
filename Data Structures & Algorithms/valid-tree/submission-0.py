class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connections = defaultdict(set)
        for a, b in edges:
            connections[a].add(b)
            connections[b].add(a)
        
        visited = set()
        q = deque()
        q.append(0)
        while q:
            l = q.popleft()
            if l in visited:
                return False
            visited.add(l)
            for c in connections[l]:
                q.append(c)
                connections[c].remove(l)
        return len(visited) == n