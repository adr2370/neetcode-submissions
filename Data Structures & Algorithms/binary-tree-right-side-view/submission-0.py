# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSide = []
        def help(root: Optional[TreeNode], level: int):
            if not root:
                return
            if level >= len(rightSide):
                rightSide.append(root.val)
            else:
                rightSide[level] = root.val
            help(root.left, level + 1)
            help(root.right, level + 1)
        help(root, 0)
        return rightSide