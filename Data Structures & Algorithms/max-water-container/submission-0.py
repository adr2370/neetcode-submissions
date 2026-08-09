class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        start, end = 0, len(heights) - 1
        while end > start:
            maximum = max(maximum, min(heights[end], heights[start]) * (end - start))
            if heights[end] < heights[start]:
                end -= 1
            else:
                start += 1
        return maximum
