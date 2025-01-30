"""This code is a faster version of the two sum array 2 code
it makes use of 2 pointers"""
"""Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] 
and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2]
 of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space."""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        right=len(numbers)-1
        left=0
        

        while right>left:
            a=numbers[left]
            b=numbers[right]
            if a+b==target:
                return [left+1,right+1]
            elif a+b>target:
                right-=1
            elif a+b<target:
                left+=1
        return []            
