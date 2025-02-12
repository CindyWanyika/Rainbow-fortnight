"""Given an integer array nums, move all 0's to the end of it while maintaining the 
relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array."""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right=1
        left=0
        if len(nums)==1:
            return nums

        for i in range(len(nums)-1):
            if nums[left]==0: 
                if nums[right]==0:
                    right+=1
                else:
                    nums[left]=nums[right]
                    nums[right]=0
                    left+=1
                    right+=1
            else:
                right+=1
                left+=1            
        return nums       

        