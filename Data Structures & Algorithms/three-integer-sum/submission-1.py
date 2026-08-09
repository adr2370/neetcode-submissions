class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        lastIndexes = {}
        for i, n in enumerate(nums):
            lastIndexes[n] = i

        triplets = {}
        for i, n0 in enumerate(nums):
            if i > 0 and nums[i-1] == n0:
                continue
            for j in range(i + 1, len(nums)):
                n1 = nums[j]
                target = 0 - n0 - n1
                if target in lastIndexes:
                    n2_index = lastIndexes[target]
                    if n2_index > j:
                        triplets[(n0, n1, target)] = True
        output = []
        for t in triplets.keys():
            output.append(list(t))
        return output