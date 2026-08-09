class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        startPositions = {}
        maximum = 0
        start_index = 0
        for i, c in enumerate(s):
            char_index = startPositions.get(c, -1)
            if char_index >= start_index:
                start_index = char_index + 1
            startPositions[c] = i
            maximum = max(maximum, i - start_index + 1)
        return maximum
