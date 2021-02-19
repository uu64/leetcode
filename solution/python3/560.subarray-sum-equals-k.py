#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = collections.defaultdict(int)
        ruiseki = ans = 0
        for n in nums:
            ruiseki += n
            if ruiseki == k:
                ans += 1
            if (ruiseki - k) in count:
                ans += count[ruiseki - k]
            count[ruiseki] += 1
        return ans
# @lc code=end

