class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        zero_index = 0

        for i in range(length):
            if nums[i] != 0:
                if i != zero_index:
                    nums[zero_index] = nums[i]
                    nums[i] = 0
                zero_index += 1
