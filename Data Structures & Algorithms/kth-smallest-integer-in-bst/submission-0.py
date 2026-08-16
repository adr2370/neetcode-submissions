# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Return a tuple of the number of nodes and the kth smallest
        def help(root, k):
            if not root:
                return (0, None)
            (left_count, left_ans) = help(root.left, k)
            if left_ans:
                return (0, left_ans)
            if left_count == k - 1:
                return (0, root.val)
            (right_count, right_ans) = help(root.right, k - left_count - 1)
            if right_ans:
                return (0, right_ans)
            return (left_count + right_count + 1, None)
        return help(root, k)[1]