#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    ans += 1
                    self.dfs(grid, i, j)
        return ans

    def dfs(self, grid, i, j):
        grid[i][j] = 0
        if i > 0 and grid[i-1][j] == "1":
            self.dfs(grid, i-1, j)
        if i < len(grid) - 1 and grid[i+1][j] == "1":
            self.dfs(grid, i+1, j)
        if j > 0 and grid[i][j-1] == "1":
            self.dfs(grid, i, j-1)
        if j < len(grid[i]) - 1 and grid[i][j+1] == "1":
            self.dfs(grid, i, j+1)

# @lc code=end

