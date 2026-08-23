# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        copy_node = Node(node.val)
        nodes = {node.val: copy_node}
        queue = deque([node])
        connections = {}
        while queue:
            curr = queue.pop()
            connections[curr.val] = curr.neighbors
            for n in curr.neighbors:
                if n.val not in nodes:
                    nodes[n.val] = Node(n.val)
                    queue.append(n)
        for k, v in connections.items():
            n = []
            for neighbhor in v:
                n.append(nodes[neighbhor.val])
            nodes[k].neighbors = n
        return copy_node

