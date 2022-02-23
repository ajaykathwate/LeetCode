"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        newNode = Node(node.val, [])
        visited = {node.val: newNode}
        def dfs(curr, node):
            for n in node.neighbors:
                if visited.get(n.val) is None:
                    newNode = Node(n.val, [])
                    visited[n.val] = newNode
                    curr.neighbors.append(newNode) 
                    dfs(newNode, n)
                else:
                    curr.neighbors.append(visited[n.val])
        dfs(newNode, node)
        return newNode