#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf') for j in range(amount+1)] for i in range(len(coins))]
        for i in range(len(coins)):
            for j in range(amount+1):
                if j == 0:
                    dp[i][j] = 0
                if i > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j])
                if j >= coins[i]:
                    dp[i][j] = min(dp[i][j - coins[i]] + 1, dp[i][j])

        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1

# @lc code=end

