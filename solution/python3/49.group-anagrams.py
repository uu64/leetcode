#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            if not len(s) in d:
                d[len(s)] = []

            d[len(s)].append(s)

        ans = []
        for s in strs:
            group = []
            tmp = d[len(s)][:]
            for word in tmp:
                if ''.join(sorted(s)) == ''.join(sorted(word)):
                    d[len(s)].remove(word)
                    group.append(word)
            if len(group) != 0:
                ans.append(group)
        return ans
# @lc code=end