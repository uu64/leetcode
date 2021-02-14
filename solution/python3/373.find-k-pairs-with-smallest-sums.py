#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        uv = []
        for i in nums1:
            for j in nums2:
                uv.append((i, j))

        ans = []
        for v in heapq.nsmallest(k, uv, key=sum):
            ans.append(list(v))
        return ans

# @lc code=end

