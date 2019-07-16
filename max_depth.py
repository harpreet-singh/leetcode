# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        maxl = self.maxDepth(root.left) + 1
        maxr = self.maxDepth(root.right)+1       
        return maxl if maxl > maxr else maxr

