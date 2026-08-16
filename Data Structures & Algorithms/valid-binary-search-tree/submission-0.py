# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def help(root: Optional[TreeNode], minRequired: int, maxRequired: int):
            if not root:
                return True
            if root.val >= minRequired or root.val <= maxRequired:
                return False
            return help(root.left, root.val, maxRequired) and help(root.right, minRequired, root.val)
        return help(root, 1000000001, -1000000001)