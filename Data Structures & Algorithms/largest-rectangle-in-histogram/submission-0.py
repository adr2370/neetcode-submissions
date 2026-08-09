class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_so_far = 0
        stack = []
        for h in heights:
            previous_higher = 0
            while stack and stack[-1][0] > h:
                previous_higher += stack[-1][1] + 1
                max_so_far = max(max_so_far, previous_higher * stack[-1][0])
                stack.pop()
            stack.append((h, previous_higher))
        previous_higher = 0
        while stack:
            previous_higher += stack[-1][1] + 1
            max_so_far = max(max_so_far, previous_higher * stack[-1][0])
            stack.pop()
        return max_so_far