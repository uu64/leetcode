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
        isValid = True
        if root:
            if root.left:
                isValid = isValid and root.left.val < root.val
            if root.right:
                isValid = isValid and root.val < root.right.val

            return isValid and self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return isValid

    def search(self, root, minVal, maxVal):
        isValid = True
        if root:
            if root.left:
                l = self.search(root.left, minVal, maxVal)
                isValid = isValid and l[0] and l[2] < root.val and root.val < l[1]
            if root.right:
                l = self.search(root.right, minVal, maxVal)
                isValid = isValid and l[0] and l[2] < root.val and root.val < l[1]
        else:
            return (isValid, minVal, maxVal)
# @lc code=end

