#You are given an integer array nums. You are initially positioned at the array's first index,
#  and each element in the array represents your maximum jump length at that position.

#Return true if you can reach the last index, or false otherwise.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jump=nums[0]
        for i in range(1,len(nums)):
            if jump==0:
                return False
            jump-=1
            jump=max(jump,nums[i])    
        return True    