class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2
        
        s1, e1 = 0, m
        while s1 <= e1:
            m1 = (s1 + e1) // 2
            m2 = half_len - m1
            
            maxLeft1 = nums1[m1-1] if m1 > 0 else float('-inf')
            minRight1 = nums1[m1] if m1 < m else float('inf')
            maxLeft2 = nums2[m2-1] if m2 > 0 else float('-inf')
            minRight2 = nums2[m2] if m2 < n else float('inf')
            
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            elif maxLeft1 > minRight2:
                e1 = m1 - 1
            else:
                s1 = m1 + 1
        return 0.0