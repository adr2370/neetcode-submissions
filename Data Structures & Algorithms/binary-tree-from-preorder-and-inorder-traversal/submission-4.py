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
        self.start_pre = 0
        def help(start_in, end_in):
            if start_in >= end_in:
                return None
            i = self.start_pre
            self.start_pre += 1
            j = ino[preorder[i]]
            l, r = help(max(0, start_in), j), help(j + 1, min(end_in, len(inorder)))
            return TreeNode(preorder[i], l, r)
        return help(0, len(inorder))
        