# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def areNodesSymmetric(self, root1, root2):
        if root1 is None or root2 is None:
            return root1 == root2
        if root1.val != root2.val:
            return False
        return self.areNodesSymmetric(root1.left, root2.right) and self.areNodesSymmetric(root1.right, root2.left) and self
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.areNodesSymmetric(root.left, root.right)

        