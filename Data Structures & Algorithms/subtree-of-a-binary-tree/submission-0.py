# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def helper(root: Optional[TreeNode], subRoot: Optional[TreeNode], mustMatch: bool) -> bool:
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if not (root and subRoot and root.val != subRoot.val):
                if helper(root.left, subRoot.left, True) and helper(root.right, subRoot.right, True):
                    return True
            if mustMatch:
                return False
            return helper(root.left, subRoot, False) or helper(root.right, subRoot, False)
            
        return helper(root, subRoot, False)