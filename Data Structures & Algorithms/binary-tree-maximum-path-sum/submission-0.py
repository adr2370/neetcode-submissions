# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_so_far = root.val
        def help(root):
            nonlocal max_so_far
            if not root:
                return 0
            l, r = help(root.left), help(root.right)
            max_so_far = max(max_so_far, l + r + root.val)
            return max(l + root.val, r + root.val, root.val, 0)
        help(root)
        return max_so_far