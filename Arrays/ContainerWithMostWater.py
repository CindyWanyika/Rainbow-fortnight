"""You are given an integer array height of length n. There are n vertical lines drawn
 such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."""
class Solution:  
    def maxArea(self, height: list[int]) -> int:
        largest=0
        left=0
        right=len(height)-1

        while True:
            if left==right:
                break
            h=min(height[left],height[right])
            area=(right-left)*h
            if area>largest:largest=area
            if height[left]>=height[right]:
                right-=1
            else:
                left+=1   

        return largest        
