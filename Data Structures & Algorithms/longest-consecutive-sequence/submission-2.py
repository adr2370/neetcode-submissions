class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = {}
        for n in nums:
            longest[n] = False

        output = 0
        for key, value in longest.items():
            if value:
                continue
            curr_output = 1
            i = key
            while i + 1 in longest:
                curr_output += 1
                i += 1
                longest[i] = True

            i = key
            while i - 1 in longest:
                curr_output += 1
                i -= 1
                longest[i] = True
            longest[key] = True
            output = max(output, curr_output)

        return output