#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        root = int(len(nums) / 2)
        left = self.sortedArrayToBST(nums[:root])
        right = self.sortedArrayToBST(nums[root+1:])
        return TreeNode(nums[root], left, right)

# @lc code=end

