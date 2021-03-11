#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        memo = [0 for i in range(N)]
        memo[0] = nums[0]
        for i in range(N):
            maxSum = nums[i]
            for j in range(0, max(0, i - 1)):
                if maxSum < memo[j] + nums[i]:
                    maxSum = memo[j] + nums[i]
            memo[i] = maxSum
        return max(memo[-2:])




# @lc code=end

