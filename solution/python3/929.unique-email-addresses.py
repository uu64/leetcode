#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
import collections
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        note = collections.defaultdict(set)
        for mail in emails:
            tmp = mail.split("@")
            note[tmp[1]].add(tmp[0].split("+")[0].replace(".", ""))

        ans = 0
        for v in note.values():
            ans += len(v)
        return ans
# @lc code=end

