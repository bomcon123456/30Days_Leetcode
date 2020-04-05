import math


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -math.inf
        s = 0
        for i in range(0, len(nums)):
            s += nums[i]
            if s > res:
                res = s
            if s < 0:
                s = 0
        return res
