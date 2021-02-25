#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.dfs(root, 0, targetSum)

    def dfs(self, node, current, target):
        if node:
            current += node.val
            if node.left is None and node.right is None and current == target:
                return True
            return self.dfs(node.left, current, target) or self.dfs(node.right, current, target)

        else:
            return False
# @lc code=end

