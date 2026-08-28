class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(set)
        reqs = defaultdict(set)
        for p in prerequisites:
            prereqs[p[0]].add(p[1])
            reqs[p[1]].add(p[0])

        queue = deque()
        for r in range(numCourses):
            if len(prereqs[r]) == 0:
                queue.append(r)
        while queue:
            n = queue.popleft()
            for r in reqs[n]:
                prereqs[r].remove(n)
                if len(prereqs[r]) == 0:
                    queue.append(r)

        for p in prereqs.values():
            if len(p) != 0:
                return False
        return True
