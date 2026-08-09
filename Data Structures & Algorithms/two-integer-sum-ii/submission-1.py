class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while end > start:
            s = numbers[start] + numbers[end]
            if s > target:
                end -= 1
            elif s < target:
                start += 1
            else:
                return [start + 1, end + 1]
