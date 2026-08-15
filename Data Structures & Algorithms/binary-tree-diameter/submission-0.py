# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.help(root)[0] - 1

    # return max diameter and max height
    def help(self, root: Optional[TreeNode]) -> (int, int):
        if not root:
            return (0, 0)
        (dia_left, height_left) = self.help(root.left)
        (dia_right, height_right) = self.help(root.right)
        return (max(dia_left, dia_right, 1 + height_left + height_right), 1 + max(height_left, height_right))