"""You have a long flowerbed in which some of the plots are planted, and some are not. However,
 flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the 
no-adjacent-flowers rule and false otherwise."""

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        tot=len(flowerbed)
        prev=0

        for i in range(tot):
            if flowerbed[i]==0 and prev==0:
                n-=1
                flowerbed[i]=1
            if flowerbed[i]==1 and prev==1:
                n+=1 
            prev=flowerbed[i]
            
        if n<=0:return True
        else: return False      