class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nextCourses = deque()
        prereqMap = defaultdict(int)
        reqMap = defaultdict(set)
        for p in prerequisites:
            prereqMap[p[0]] += 1
            reqMap[p[1]].add(p[0])
        for i in range(numCourses):
            if prereqMap[i] == 0:
                nextCourses.append(i)
        ans = []
        while nextCourses:
            n = nextCourses.popleft()
            ans.append(n)
            for r in reqMap[n]:
                prereqMap[r] -= 1
                if prereqMap[r] == 0:
                    nextCourses.append(r)
        if len(ans) == numCourses:
            return ans
        return[]