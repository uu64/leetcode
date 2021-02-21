#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    if ans < area:
                        ans = area
        return ans

    def dfs(self, grid, i, j):
        grid[i][j] = 0
        count = 1

        if i > 0 and grid[i-1][j] == 1:
            count += self.dfs(grid, i-1, j)

        if i < len(grid) - 1 and grid[i+1][j] == 1:
            count += self.dfs(grid, i+1, j)

        if j > 0 and grid[i][j-1] == 1:
            count += self.dfs(grid, i, j-1)

        if j < len(grid[i]) - 1 and grid[i][j+1] == 1:
            count += self.dfs(grid, i, j+1)

        return count

# @lc code=end

