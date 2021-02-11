#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        ans = 0
        while True:
            if start == end:
                break

            area = (end - start) * min(height[start], height[end])
            if ans < area:
                ans = area
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return ans

# @lc code=end

