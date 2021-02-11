#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        max = ans =  100000
        print(nums)

        for i, v in enumerate(nums):
            print(v)
            if i == len(nums) - 2:
                if max > abs(target - prev):
                    max = abs(target - prev)
                    ans = prev
                break

            l = i + 1
            r = len(nums) - 1

            prev = v + nums[l] + nums[r]

            while True:

                if target > prev:
                    l += 1
                elif target < prev:
                    r -= 1
                else:
                    max = 0
                    ans = prev
                    break

                if r <= l:
                    if max > abs(target - prev):
                        max = abs(target - prev)
                        ans = prev
                    break

                s = v + nums[l] + nums[r]
                if max > abs(target - prev):
                    max = abs(target - prev)
                    ans = prev

                prev = s

        return ans:

# @lc code=end

