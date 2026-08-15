# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def help(root: Optional[TreeNode]) -> int:
            nonlocal ans
            if not root:
                return 0
            l, r = help(root.left), help(root.right)
            if not (-1 <= l - r <= 1):
                 ans = False
            return max(l, r) + 1
        help(root)
        return ans