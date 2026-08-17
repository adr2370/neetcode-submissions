class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            heap.append(((p[0]**2 + p[1]**2)**0.5, p))
        heapq.heapify(heap)
        output = heapq.nsmallest(k, heap)
        ans = []
        for o in output:
            ans.append(o[1])
        return ans