#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        offset = 0
        while(len(nums) > 1):
            pivot = len(nums) // 2
            if nums[pivot] > target:
                nums = nums[:pivot]
            else:
                offset += pivot
                nums = nums[pivot:]

        if nums[0] > target:
            return max(0, offset - 1)
        elif nums[0] < target:
            return offset + 1
        else:
            return offset


# @lc code=end

