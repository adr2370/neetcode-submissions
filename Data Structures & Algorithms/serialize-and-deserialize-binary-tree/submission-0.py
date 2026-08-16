# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        delim = "#"
        q = deque()
        q.append(root)
        ans = ""
        while q:
            c = q.popleft()
            if c:
                ans += str(c.val)
                q.append(c.left)
                q.append(c.right)
            ans += delim
        return ans
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        delim = "#"
        pointer = 0
        ans = None
        q = deque()
        left_next = True
        while pointer < len(data):
            next_p = pointer
            while data[next_p] != delim:
                next_p += 1
            node = None
            if next_p > pointer:
                v = int(data[pointer:next_p])
                node = TreeNode(v)
                q.append(node)
            if ans == None:
                ans = node
            elif left_next:
                q[0].left = node
                left_next = False
            else:
                q.popleft().right = node
                left_next = True
            pointer = next_p + 1
        return ans

