#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, v in enumerate(nums):

            if i > 0 and v == nums[i-1]:
                continue

            a = v
            l = i + 1
            r = len(nums) - 1

            while True:
                if l >= r:
                    break
                s = a + nums[l] + nums[r]

                if s > 0:
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1

                elif s < 0:
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                else:
                    ans.append([a, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1

# @lc code=end

