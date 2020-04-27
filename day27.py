class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        m, n, max_len, c = len(matrix), len(matrix[0]), 0, 0
        dp = [0] * (n+1)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[j+1], c = min(dp[j], dp[j+1], c) + 1, dp[j+1]
                    max_len = max(max_len, dp[j+1])
                else:
                    dp[j+1], c = 0, dp[j+1]
        return max_len * max_len
