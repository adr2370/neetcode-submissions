class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        l, l_len, r_len = -self.left[0] if self.left else None, len(self.left), len(self.right)
        if l == None or num <= l:
            heapq.heappush(self.left, -num)
            if l_len > r_len:
                v = -heapq.heappop(self.left)
                heapq.heappush(self.right, v)
        else:
            heapq.heappush(self.right, num)
            if l_len == r_len:
                v = heapq.heappop(self.right)
                heapq.heappush(self.left, -v)

    def findMedian(self) -> float:
        l, r, l_len, r_len = -self.left[0] if self.left else None, self.right[0] if self.right else None, len(self.left), len(self.right)
        return (l + r) / 2.0 if l_len == r_len else l


        