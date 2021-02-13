#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
class KthLargest:
    k = -1
    stream = -1

    def __init__(self, k: int, nums: List[int]):
        tmp = sorted(nums)
        self.stream = tmp[-k:]
        self.k = k

    def add(self, val: int) -> int:
        tmp = self.stream[:]
        tmp.append(val)
        self.stream = sorted(tmp)[-self.k:]
        return self.stream[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

