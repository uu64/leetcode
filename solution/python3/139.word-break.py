#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False for i in range(len(s)+1)]
        memo[0] = True

        for i in range(1, len(s)+1):
            for j in range(0, i):
                tmp = s[j:i]
                if memo[j] and tmp in wordDict:
                    memo[i] = True
                    break

        return memo[len(s)]

# @lc code=end

