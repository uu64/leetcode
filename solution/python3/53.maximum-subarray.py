#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ruiseki = maxSum = minSum = nums[0]
        for i in range(1, len(nums)):
            ruiseki += nums[i]
            maxSum = max(ruiseki, ruiseki - minSum, maxSum)
            minSum = min(ruiseki, minSum)

        return maxSum
# @lc code=end

