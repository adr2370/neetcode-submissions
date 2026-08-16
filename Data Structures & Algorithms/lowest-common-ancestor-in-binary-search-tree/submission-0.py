# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Return if p is present in the tree, q is present in the tree, and the lowest common ancestor if found
        def help(root: TreeNode, p: TreeNode, q: TreeNode):
            if not root:
                return (False, False, None)
            l, r = help(root.left, p, q), help(root.right, p, q)
            if l[2]:
                return (False, False, l[2])
            if r[2]:
                return (False, False, r[2])
            p_found = l[0] or r[0] or root == p
            q_found = l[1] or r[1] or root == q
            if p_found and q_found:
                return (False, False, root)
            return (p_found, q_found, None)

        return help(root, p, q)[2]