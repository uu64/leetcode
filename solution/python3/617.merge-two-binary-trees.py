#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 or root2:
            node = TreeNode()
            val1 = root1.val if root1 else 0
            val2 = root2.val if root2 else 0
            node.val = val1 + val2
            node.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
            node.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
            return node
        else:
            return None


# @lc code=end

