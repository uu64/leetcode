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
                d[len(s)] = {}

            if s[0] in d[len(s)]:
                d[len(s)][s[0]].append(s)
            else:
                d[len(s)][s[0]] = [s]

        ans = []
        for s in strs:
            words = d[len(s)]
            group = []
            for c in s:
                tmp = words[c][:]
                for word in tmp:
                    if Counter(s) == Counter(word):
                        words[c].remove(s)
                        group.append(s)
            ans.append(group)
        return ans
# @lc code=end