#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root:
            return self.bfs([root], 1)
        else:
            return 0


    def bfs(self, queue, depth):
        newQueue = []

        for node in queue:
            if node.left is None and node.right is None:
                return depth

            if node.left:
                newQueue.append(node.left)

            if node.right:
                newQueue.append(node.right)

        return self.bfs(newQueue, depth + 1)

# @lc code=end

