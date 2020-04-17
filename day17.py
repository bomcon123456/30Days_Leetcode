class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        land = set()
        res = 0

        def dfs(r, c):
            if (r, c) in land:
                land.remove((r, c))
                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    land.add((i, j))

        while land:
            l = land.pop()
            land.add(l)

            dfs(l[0], l[1])
            res += 1
        return res
