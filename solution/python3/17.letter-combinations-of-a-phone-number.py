#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []

        if len(digits) == 0:
            return ans

        queue = []
        for c in digits:
            queue.append(int(c))
        return self.main([""], queue)


    def main(self, prefixList, queue):
        if len(queue) == 0:
            return prefixList

        digitsMap = {
            1: [],
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }

        n = queue.pop(0)

        chars = digitsMap[n]
        newPrefixList = []
        for c in chars:
            for pre in prefixList:
                newPrefixList.append(pre + c)

        return self.main(newPrefixList, queue)



# @lc code=end

