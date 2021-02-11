#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        ans = 0
        if len(s) == 0:
            return ans

        while True:
            end = end + 1

            if end == len(s):
                if ans < end - start:
                    ans = end - start
                break

            if s[end] in s[start:end]:
                if ans < end - start:
                    ans = end - start
                start = start + s[start:end].find(s[end]) + 1
        return ans

# @lc code=end

