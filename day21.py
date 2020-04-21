class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()

        def check_row_has_one(column):
            return any(binaryMatrix.get(i, column) for i in range(m))

        lo = 0
        hi = n

        while lo < hi:
            mid = (lo + hi) // 2
            if check_row_has_one(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo if lo < n else -1
