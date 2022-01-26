# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, lst, node):
        if not node:
            return 
        else:
            self.inorder(lst, node.left)
            lst.append(node.val)
            self.inorder(lst,node.right)
        return lst
    
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list_ = []
        self.inorder(list_,root1)
        self.inorder(list_,root2)
        return sorted(list_)