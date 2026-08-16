# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        def help(root: Optional[TreeNode], level: int, levels: List[List[int]]):
            if not root:
                return
            if level >= len(levels):
                levels.append([])
            levels[level].append(root.val)
            help(root.left, level + 1, levels)
            help(root.right, level + 1, levels)
        help(root, 0, levels)
        return levels