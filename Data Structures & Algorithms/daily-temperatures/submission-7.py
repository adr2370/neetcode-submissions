class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack:
                (j, t0) = stack[-1]
                if t0 < t:
                    stack.pop()
                    output[j] = i - j
                else:
                    break
            stack.append((i, t))
        return output