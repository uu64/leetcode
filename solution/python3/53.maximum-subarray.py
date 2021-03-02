#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ruiseki = [nums[0]]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            ruiseki.append(ruiseki[i-1] + nums[i])
            maxSum = max(ruiseki[i], ruiseki[i] - min(ruiseki[:i]), maxSum)

        return maxSum
# @lc code=end

