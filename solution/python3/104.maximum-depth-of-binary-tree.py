#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxd = 0
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            self.dfs(root, 1)
        return self.maxd

    def dfs(self, node, depth):
        if node.left is None and node.right is None:
            if self.maxd < depth:
                self.maxd = depth
            return

        if node.left:
            self.dfs(node.left, depth + 1)

        if node.right:
            self.dfs(node.right, depth + 1)



# @lc code=end

