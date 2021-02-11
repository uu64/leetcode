#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        symbolMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        ans = 0

        prev = 1000
        for c in s:
            n = symbolMap[c]
            if prev < n:
                ans = ans - prev + (n - prev)
            else:
                ans += n
            prev = n
        return ans

# @lc code=end

