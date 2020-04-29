import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        d[0] = 1
        s = 0
        count = 0
        for i in range(0, len(nums)):
            s += nums[i]
            if s-k in d:
                count += d[s-k]
            d[s] += 1
        return count