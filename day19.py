      def search(self, nums: List[int], target: int) -> int:
        def bisearch(l,r):
            if l > r:
                return -1
            m = (r+l)//2
            if nums[m] == target:
                return m
            if nums[l] <= target < nums[m] or (nums[m] <= nums[r]  and not nums[m] < target <= nums[r]):
                return bisearch(l,m-1)
            else: 
                return bisearch(m+1, r)
        return bisearch(0,len(nums)-1)