# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def help(root: TreeNode, maxSoFar: int):
            if not root:
                return 0
            return (1 if root.val >= maxSoFar else 0) + help(root.left, max(maxSoFar, root.val)) + help(root.right, max(maxSoFar, root.val))
        if not root:
            return 0
        return 1 + help(root.left, root.val) + help(root.right, root.val)
