#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()

        for a in nums:
            tmp = nums[:]
            tmp.remove(a)
            print(tmp)

            for i,b in enumerate(tmp):
                if i == len(tmp) - 2:
                    break

                l = i + 1
                r = len(tmp) - 1

                while True:
                    if l >= r:
                        break

                    c = tmp[l]
                    d = tmp[r]

                    if b + c + d < target - a:
                        while l+1 < len(tmp) and tmp[l] == tmp[l+1]:
                            l += 1
                        l += 1
                    elif b + c + d > target -a:
                        while r-1 > 0 and tmp[r-1] == tmp[r] :
                            r -= 1
                        r -= 1
                    else:
                        ans.add(tuple(sorted([a, b, c, d])))
                        while l+1 < len(tmp) and tmp[l] == tmp[l+1]:
                            l += 1
                        l += 1

        return ans

# @lc code=end

