class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while n > m:
            n &= (n-1)     # setting the lowest `1-bit` of n to 0 
        return n