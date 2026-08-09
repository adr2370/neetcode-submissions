class Solution:
    def trap(self, height: List[int]) -> int:
        maxHeight = max(height)
        maxIndex = height.index(maxHeight)
        latestPeak = 0
        rain = 0
        for i in range(0, maxIndex):
            rain += max(latestPeak - height[i], 0)
            latestPeak = max(latestPeak, height[i])
        latestPeak = 0
        for i in range(len(height)-1, maxIndex, -1):
            rain += max(latestPeak - height[i], 0)
            latestPeak = max(latestPeak, height[i])
        return rain