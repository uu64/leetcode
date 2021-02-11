#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            for j in range(0, len(s)-i+1):
                tmp = s[j:j+i]
                if tmp == tmp[::-1]:
                    return tmp

# @lc code=end

