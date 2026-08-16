class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.n = [float("-inf")] * k
        for v in nums:
            self.add(v)

    def add(self, val: int) -> int:
        m = self.n[0]
        if val > m:
            heapq.heappop(self.n)
            heapq.heappush(self.n, val)
        return self.n[0]
