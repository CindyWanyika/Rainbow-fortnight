"""Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation."""
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products=[0]*len(nums)
        pref=1
        for i in range(len(nums)):
            products[i]=pref
            pref*=nums[i]
        suff=1    
        n=len(nums)-1    
        while n>=0:
            products[n]*=suff
            suff*=nums[n]
            n-=1

        return products   

        