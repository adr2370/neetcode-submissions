# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ino = {}
        for i, p in enumerate(inorder):
            ino[p] = i
        def help(start_pre, start_in, end_in):
            if start_in >= end_in:
                return None
            first_i = -1
            for i in range(start_pre, len(preorder)):
                if start_in <= ino[preorder[i]] < end_in:
                    first_i = i
                    break
            j = ino[preorder[i]]
            l, r = help(first_i + 1, max(0, start_in), j), help(first_i + 1, j + 1, min(end_in, len(inorder)))
            return TreeNode(preorder[first_i], l, r)
        return help(0, 0, len(inorder))
        