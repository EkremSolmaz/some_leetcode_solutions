# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMaxInTree(self, node):
        if not node.right:
            return node
        else:
            return self.findMaxInTree(node.right)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            left = root.left
            right = root.right
            if left and right:
                replacement = self.findMaxInTree(left)
                temp = root.val
                root.val = replacement.val
                replacement.val = temp
                root.left = self.deleteNode(left, key)

                return root

            return right if not left else left
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root
