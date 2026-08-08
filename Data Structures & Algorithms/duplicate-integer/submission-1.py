class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = defaultdict(bool)
        for n in nums:
            if c[n]:
                return True
            else:
                c[n] = True
        return False