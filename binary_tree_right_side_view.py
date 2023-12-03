# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getRightView(self, node: Optional[TreeNode]):
        if node is None:
            return []
        l = self.getRightView(node.left)
        r = self.getRightView(node.right)
        if(len(l) > len(r)):
            return [node.val] + r[:len(l)] + l[len(r):]
        return [node.val] + r
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.getRightView(root)