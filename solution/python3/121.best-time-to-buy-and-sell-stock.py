#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
import heapq

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        minPrice = prices[0]
        ans = 0
        for p in prices:
            if p - minPrice > ans:
                ans = p - minPrice
            if p < minPrice:
                minPrice = p

        return ans

# @lc code=end

