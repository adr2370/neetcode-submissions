class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(2**len(nums)):
            c = []
            for j in range(len(nums)):
                if i % 2 == 1:
                    c.append(nums[j])
                i = i >> 1
            output.append(c)
        return output