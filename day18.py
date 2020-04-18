class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0]) if grid else 0
        for r in range(n):
            for c in range(m):
                if r == 0 and c == 0:
                    continue
                elif r == 0:
                    grid[r][c] += grid[r][c-1]
                elif c == 0:
                    grid[r][c] += grid[r-1][c]
                else:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        return grid[n-1][m-1]
