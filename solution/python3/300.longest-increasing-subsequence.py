#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        memo[nums[0]] = 1
        for i in range(1, len(nums)):
            maxLen = 0
            for j in range(i):
                if nums[j] < nums[i] and maxLen < memo[nums[j]]:
                    maxLen = memo[nums[j]]
            memo[nums[i]] = maxLen + 1

        # print(memo)
        return sorted(memo.items(), key=lambda x:x[1], reverse=True)[0][1]

# @lc code=end
