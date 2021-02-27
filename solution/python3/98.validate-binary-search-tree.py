#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        leaves = []
        result = self.pickLeaves(root, leaves)
        for i in range(1, len(leaves)):
            if leaves[i-1] >= leaves[i]:
                return False
        return True

    def pickLeaves(self, root, leaves):
        if root:
            self.pickLeaves(root.left, leaves)
            leaves.append(root.val)
            self.pickLeaves(root.right, leaves)


# @lc code=end

