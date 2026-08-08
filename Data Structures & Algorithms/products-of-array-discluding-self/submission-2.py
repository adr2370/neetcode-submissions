class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                total_product *= n
        output = []
        for n in nums:
            if zero_count > 1:
                output.append(0)
            elif zero_count == 1:
                if n == 0:
                    output.append(total_product)
                else:
                    output.append(0)
            else:
                output.append(total_product//n)
        return output