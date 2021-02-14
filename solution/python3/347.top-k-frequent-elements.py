#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        tmp = {}
        count = 0
        nums.sort()
        for i in range(len(nums)):
            count += 1
            if i == len(nums) - 1 or nums[i] != nums[i+1]:
                heapq.heappush(heap, count)
                if count in tmp:
                    tmp[count].append(nums[i])
                else:
                    tmp[count] = [nums[i]]
                count = 0

        print(tmp)
        ans = []
        for i in heapq.nlargest(k, heap):
            ans.extend(tmp[i])
        return set(ans)

# @lc code=end

