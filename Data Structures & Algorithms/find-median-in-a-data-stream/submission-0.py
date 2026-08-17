from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.nums = SortedList()

    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        l = len(self.nums)
        if l % 2 == 1:
            return self.nums[l // 2]
        m = l // 2
        return (self.nums[m - 1] + self.nums[m]) / 2.0


        