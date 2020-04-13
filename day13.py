class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        d[0] = -1
        count = 0
        res = 0
        for i in range(len(nums)):
            count += 1 if nums[i] else -1
            if count in d:
                res = max(res, i-d[count])
            else:
                d[count] = i
        return res
