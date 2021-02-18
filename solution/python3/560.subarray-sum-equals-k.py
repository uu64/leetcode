#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = {}
        ans = 0
        for i in range(len(nums)):
            for j in range(len(nums) - i):
                tmp = tuple(sorted(nums[j:j+i+1]))
                if not tmp in memo:
                    memo[tmp] = sum(tmp)

                if memo[tmp] == k:
                    ans += 1
        return ans
# @lc code=end

