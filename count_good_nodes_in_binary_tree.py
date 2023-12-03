# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def howManyGoodChild(self, node, max_so_far):
        if node is None:
            return 0
        max_so_far = max(max_so_far, node.val)
        return int(node.val >= max_so_far) + self.howManyGoodChild(node.left, max_so_far) + self.howManyGoodChild(node.right, max_so_far)
        
    def goodNodes(self, root: TreeNode) -> int:
        return self.howManyGoodChild(root, -10000)

        